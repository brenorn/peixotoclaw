import React, { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Send, Paperclip, Mic, User, Bot, FileText } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  attachment?: { type: string; name: string };
}

interface ChatWindowProps {
  selectedSkill: string | null;
  onSendMessage: (text: string, files: File[]) => Promise<void>;
  onSelectSkill: (name: string) => void;
  messages: Message[];
  isProcessing: boolean;
}

const ChatWindow: React.FC<ChatWindowProps> = ({ selectedSkill, onSendMessage, onSelectSkill, messages, isProcessing }) => {
  const [input, setInput] = useState('');
  const [files, setFiles] = useState<File[]>([]);
  const [isDraggingOver, setIsDraggingOver] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, isProcessing]);

  const handleSend = () => {
    if ((input.trim() || files.length > 0) && !isProcessing) {
      onSendMessage(input, files);
      setInput('');
      setFiles([]);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDraggingOver(false);
    const skillName = e.dataTransfer.getData('skillName');
    if (skillName && textareaRef.current) {
      const skillText = `[skill:${skillName}] `;
      const start = textareaRef.current.selectionStart;
      const end = textareaRef.current.selectionEnd;
      
      const newValue = input.substring(0, start) + skillText + input.substring(end);
      setInput(newValue);
      
      // Maintain focus and set cursor after the inserted text
      setTimeout(() => {
        if (textareaRef.current) {
          textareaRef.current.focus();
          const newCursorPos = start + skillText.length;
          textareaRef.current.setSelectionRange(newCursorPos, newCursorPos);
        }
      }, 0);
    }
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    if (e.dataTransfer.types.includes('skillName')) {
      setIsDraggingOver(true);
      e.dataTransfer.dropEffect = 'copy';
    }
  };

  const handleDragLeave = () => {
    setIsDraggingOver(false);
  };

  return (
    <div 
      className={`flex-1 flex flex-col h-full m-4 glass-panel relative overflow-hidden transition-all duration-300 ${
        isDraggingOver ? 'border-peixoto-primary shadow-[0_0_20px_rgba(255,51,102,0.3)] scale-[0.995]' : ''
      }`}
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
    >
      {/* Header */}
      <div className="p-4 border-b border-white/5 flex items-center justify-between bg-white/[0.02]">
        <div className="flex items-center gap-3">
          <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse shadow-[0_0_8px_rgba(34,197,94,0.5)]"></div>
          <span className="text-sm font-medium text-white/80">
            {selectedSkill ? `PeixotoClaw • ${selectedSkill}` : 'PeixotoClaw • Neural Engine'}
          </span>
        </div>
        <div className="text-[10px] text-white/40 font-mono tracking-tighter uppercase">
          Agent Loop Active • Iterations: 5
        </div>
      </div>

      {/* Messages Area */}
      <div ref={scrollRef} className="flex-1 overflow-y-auto p-6 space-y-6">
        <AnimatePresence>
          {messages.length === 0 && (
            <motion.div 
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="h-full flex flex-col items-center justify-center text-center max-w-md mx-auto"
            >
              <div className="w-16 h-16 bg-peixoto-primary/10 rounded-3xl flex items-center justify-center mb-4 border border-peixoto-primary/20">
                <Bot className="text-peixoto-primary" size={32} />
              </div>
              <h3 className="text-xl font-bold text-white mb-2">How can I assist you today?</h3>
              <p className="text-sm text-white/40">Select a skill from the sidebar or just start typing. I can handle code, documents, and voice commands locally.</p>
            </motion.div>
          )}

          {messages.map((msg) => (
            <motion.div
              key={msg.id}
              initial={{ opacity: 0, x: msg.role === 'user' ? 20 : -20 }}
              animate={{ opacity: 1, x: 0 }}
              className={`flex items-start gap-4 ${msg.role === 'user' ? 'flex-row-reverse' : ''}`}
            >
              <div className={`w-8 h-8 rounded-lg flex items-center justify-center border ${
                msg.role === 'user' 
                  ? 'bg-white/5 border-white/10 text-white/60' 
                  : 'bg-peixoto-primary/10 border-peixoto-primary/20 text-peixoto-primary'
              }`}>
                {msg.role === 'user' ? <User size={16} /> : <Bot size={16} />}
              </div>
              
              <div className={`max-w-[80%] space-y-2`}>
                <div className={`p-4 rounded-2xl text-sm leading-relaxed ${
                  msg.role === 'user'
                    ? 'bg-peixoto-primary text-white shadow-peixoto whitespace-pre-wrap'
                    : 'bg-white/5 border border-white/10 text-white/90 prose prose-invert prose-sm max-w-none'
                }`}>
                  {msg.role === 'user' ? (
                    msg.content
                  ) : (
                    <ReactMarkdown 
                      remarkPlugins={[remarkGfm]}
                      components={{
                        p: ({node, ...props}) => <p className="mb-2 last:mb-0" {...props} />,
                        ul: ({node, ...props}) => <ul className="list-disc ml-4 mb-2" {...props} />,
                        ol: ({node, ...props}) => <ol className="list-decimal ml-4 mb-2" {...props} />,
                        li: ({node, ...props}) => <li className="mb-1" {...props} />,
                        h1: ({node, ...props}) => <h1 className="text-lg font-bold mb-2 text-peixoto-primary" {...props} />,
                        h2: ({node, ...props}) => <h2 className="text-md font-bold mb-2 text-peixoto-primary/80" {...props} />,
                        h3: ({node, ...props}) => <h3 className="text-sm font-bold mb-1 text-peixoto-primary/70" {...props} />,
                        code: ({node, ...props}) => <code className="bg-white/10 px-1 rounded text-peixoto-primary" {...props} />,
                        pre: ({node, ...props}) => <pre className="bg-black/20 p-3 rounded-lg overflow-x-auto mb-2" {...props} />
                      }}
                    >
                      {msg.content}
                    </ReactMarkdown>
                  )}
                </div>
                {msg.attachment && (
                  <div className="flex items-center gap-2 p-2 bg-white/5 border border-white/10 rounded-xl text-xs text-white/60 w-fit">
                    <FileText size={14} />
                    <span>{msg.attachment.name}</span>
                  </div>
                )}
              </div>
            </motion.div>
          ))}

          {isProcessing && (
            <motion.div 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="flex items-start gap-4"
            >
              <div className="w-8 h-8 rounded-lg bg-peixoto-primary/10 border border-peixoto-primary/20 flex items-center justify-center text-peixoto-primary">
                <Bot size={16} />
              </div>
              <div className="bg-white/5 border border-white/10 p-4 rounded-2xl flex items-center gap-2">
                <div className="flex gap-1">
                  <span className="w-1.5 h-1.5 bg-peixoto-primary rounded-full animate-bounce [animation-delay:-0.3s]"></span>
                  <span className="w-1.5 h-1.5 bg-peixoto-primary rounded-full animate-bounce [animation-delay:-0.15s]"></span>
                  <span className="w-1.5 h-1.5 bg-peixoto-primary rounded-full animate-bounce"></span>
                </div>
                <span className="text-[10px] text-white/40 uppercase tracking-widest font-bold ml-2 italic">Agent is thinking...</span>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      {/* Input Area */}
      <div className="p-4 bg-white/[0.02] border-t border-white/5">
        <div className="max-w-4xl mx-auto flex items-end gap-3">
          <div className="flex-1 relative glass-input p-0 !border-white/5 focus-within:!border-peixoto-primary/30 flex flex-col group transition-all">
            {(() => {
              const tags = Array.from(input.matchAll(/\[skill:(.*?)\]/g)).map(m => m[1]);
              const uniqueTags = [...new Set([...tags, ...(selectedSkill ? [selectedSkill] : [])])].filter(Boolean);
              
              if (uniqueTags.length === 0) return null;
              
              return (
                <div className="px-4 pt-3 flex flex-wrap gap-2">
                  {uniqueTags.map(tag => (
                    <div key={tag} className="px-2 py-0.5 bg-peixoto-primary/20 border border-peixoto-primary/40 rounded-full text-[10px] text-peixoto-primary font-bold uppercase tracking-wider flex items-center gap-1.5 shadow-[0_0_10px_rgba(255,51,102,0.1)]">
                      <span className="w-1 h-1 bg-peixoto-primary rounded-full animate-pulse"></span>
                      Skill: {tag}
                      <button 
                        onClick={() => {
                          if (tag === selectedSkill) onSelectSkill('');
                          else setInput(prev => prev.replace(`[skill:${tag}] `, '').replace(`[skill:${tag}]`, ''));
                        }} 
                        className="ml-1 hover:text-white transition-colors"
                      >
                        ×
                      </button>
                    </div>
                  ))}
                </div>
              );
            })()}
            {files.length > 0 && (
              <div className="px-4 pt-3 flex flex-wrap gap-2">
                {files.map((f, i) => (
                  <div key={i} className="flex items-center gap-2 px-2 py-1 bg-peixoto-primary/20 border border-peixoto-primary/30 rounded-lg text-[10px] text-white">
                    <FileText size={10} />
                    <span className="truncate max-w-[100px]">{f.name}</span>
                    <button onClick={() => setFiles(files.filter((_, idx) => idx !== i))} className="hover:text-red-400">×</button>
                  </div>
                ))}
              </div>
            )}
            <textarea 
              ref={textareaRef}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault();
                  handleSend();
                }
              }}
              placeholder="Tell PeixotoClaw what to do..."
              className="w-full bg-transparent p-4 text-sm focus:outline-none resize-none max-h-40 min-h-[52px]"
              rows={1}
            />
            <div className="px-3 pb-3 flex items-center gap-2">
              <button 
                onClick={() => fileInputRef.current?.click()}
                className="p-2 text-white/40 hover:text-peixoto-primary hover:bg-peixoto-primary/10 rounded-lg transition-all"
              >
                <Paperclip size={18} />
              </button>
              <input 
                type="file" 
                ref={fileInputRef} 
                className="hidden" 
                multiple 
                onChange={(e) => {
                  if (e.target.files) setFiles([...files, ...Array.from(e.target.files)]);
                }}
              />
              <button className="p-2 text-white/40 hover:text-peixoto-primary hover:bg-peixoto-primary/10 rounded-lg transition-all">
                <Mic size={18} />
              </button>
              <div className="flex-1"></div>
              <button 
                onClick={handleSend}
                disabled={(!input.trim() && files.length === 0) || isProcessing}
                className={`peixoto-button !py-2 !px-4 flex items-center gap-2 ${(!input.trim() && files.length === 0) || isProcessing ? 'opacity-50 cursor-not-allowed scale-100' : ''}`}
              >
                <Send size={18} />
              </button>
            </div>
          </div>
        </div>
        <p className="text-[10px] text-center text-white/20 mt-3 font-mono tracking-tighter">
          Powered by Gemini 2.0 Flash • Local File System Access Enabled
        </p>
      </div>
    </div>
  );
};

export default ChatWindow;
