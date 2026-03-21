import { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import ChatWindow from './components/ChatWindow';
import SkillInstall from './components/SkillInstall';
import axios from 'axios';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
}

interface Conversation {
  id: string;
  created_at: string;
}

function App() {
  const [selectedSkill, setSelectedSkill] = useState<string | null>(null);
  const [isInstallOpen, setIsInstallOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [isProcessing, setIsProcessing] = useState(false);
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [selectedConversationId, setSelectedConversationId] = useState<string | null>(null);

  const userId = "web-user-01";

  useEffect(() => {
    fetchConversations();
  }, []);

  const fetchConversations = async () => {
    try {
      const response = await axios.get(`http://localhost:3001/api/conversations?userId=${userId}`);
      setConversations(response.data);
      
      // If we have conversations but none is selected yet, select the first one
      if (response.data.length > 0 && !selectedConversationId) {
        const firstConvId = response.data[0].id;
        setSelectedConversationId(firstConvId);
        handleSelectConversation(firstConvId);
      }
    } catch (error) {
      console.error('Error fetching conversations:', error);
    }
  };

  const handleSelectConversation = async (id: string) => {
    setSelectedConversationId(id);
    try {
      const response = await axios.get(`http://localhost:3001/api/conversations/${id}/messages`);
      const mappedMessages = response.data.map((m: any) => ({
        id: m.id.toString(),
        role: m.role,
        content: m.content
      }));
      setMessages(mappedMessages);
    } catch (error) {
      console.error('Error fetching messages:', error);
    }
  };

  const handleNewChat = async () => {
    try {
      const response = await axios.post('http://localhost:3001/api/conversations/new', { userId });
      const newId = response.data.id;
      setMessages([]);
      setSelectedConversationId(newId);
      fetchConversations();
    } catch (error) {
      console.error('New Chat Error:', error);
    }
  };

  const handleSendMessage = async (text: string, files: File[]) => {
    const userMsg: Message = { id: Date.now().toString(), role: 'user', content: text };
    setMessages(prev => [...prev, userMsg]);
    setIsProcessing(true);

    try {
      const formData = new FormData();
      formData.append('userId', userId);
      formData.append('text', text);
      if (selectedSkill) formData.append('skill', selectedSkill);
      if (selectedConversationId) formData.append('conversationId', selectedConversationId);
      files.forEach(f => formData.append('files', f));

      const response = await axios.post('http://localhost:3001/api/chat', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });

      const assistantMsg: Message = { 
        id: (Date.now() + 1).toString(), 
        role: 'assistant', 
        content: response.data.content 
      };
      setMessages(prev => [...prev, assistantMsg]);
    } catch (error) {
      console.error('Chat Error:', error);
      setMessages(prev => [...prev, { 
        id: (Date.now() + 1).toString(), 
        role: 'assistant', 
        content: "⚠️ Error connecting to PeixotoClaw backend. Ensure the server is running." 
      }]);
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="flex h-screen w-full bg-peixoto-dark bg-gradient-peixoto overflow-hidden">
      <Sidebar 
        selectedSkill={selectedSkill} 
        onSelectSkill={setSelectedSkill} 
        onInstallClick={() => setIsInstallOpen(true)}
        conversations={conversations}
        selectedConversationId={selectedConversationId}
        onSelectConversation={handleSelectConversation}
        onNewChat={handleNewChat}
      />
      <main className="flex-1 flex flex-col h-full">
        <ChatWindow 
          selectedSkill={selectedSkill} 
          messages={messages}
          isProcessing={isProcessing}
          onSendMessage={handleSendMessage}
          onSelectSkill={setSelectedSkill}
        />
      </main>

      {isInstallOpen && (
        <SkillInstall 
          onClose={() => setIsInstallOpen(false)}
          onSuccess={() => {
            // Force sidebar refresh would be better, but simple reload for now
            window.location.reload();
          }}
        />
      )}

      {/* Background Glows */}
      <div className="fixed top-[-10%] left-[-10%] w-[40%] h-[40%] bg-peixoto-primary/10 blur-[120px] rounded-full pointer-events-none"></div>
      <div className="fixed bottom-[-10%] right-[-10%] w-[30%] h-[30%] bg-peixoto-accent/10 blur-[100px] rounded-full pointer-events-none"></div>
    </div>
  );
}

export default App;
