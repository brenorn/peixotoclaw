import React, { useState, useEffect } from 'react';
import { ChefHat, Code, Plus, Check, Brain, Settings, Trash2, Folder } from 'lucide-react';
import axios from 'axios';

interface Skill {
  name: string;
  description: string;
}

interface Conversation {
  id: string;
  created_at: string;
}

interface Project {
  id: string;
  name: string;
}

interface SidebarProps {
  selectedSkill: string | null;
  onSelectSkill: (name: string) => void;
  onInstallClick: () => void;
  conversations: Conversation[];
  selectedConversationId: string | null;
  onSelectConversation: (id: string) => void;
  onDeleteConversation: (id: string, e: React.MouseEvent) => void;
  onNewChat: () => void;
  projects: Project[];
  selectedProjectId: string | null;
  onSelectProject: (id: string) => void;
}

const Sidebar: React.FC<SidebarProps> = ({ 
  selectedSkill, 
  onSelectSkill, 
  onInstallClick,
  conversations,
  selectedConversationId,
  onSelectConversation,
  onDeleteConversation,
  onNewChat,
  projects,
  selectedProjectId,
  onSelectProject
}) => {
  const [skills, setSkills] = useState<Skill[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchSkills();
  }, []);

  const fetchSkills = async () => {
    try {
      const response = await axios.get('http://localhost:3001/api/skills');
      const sortedSkills = response.data.sort((a: Skill, b: Skill) => 
        a.name.localeCompare(b.name)
      );
      setSkills(sortedSkills);
    } catch (error) {
      console.error('Error fetching skills:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-80 h-full glass-panel flex flex-col p-4 m-4 mr-0">
      <div className="flex items-center justify-between mb-8 px-2">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-peixoto-primary rounded-lg flex items-center justify-center shadow-peixoto">
            <ChefHat className="text-white" size={24} />
          </div>
          <h1 className="text-xl font-bold tracking-tight text-white">PeixotoClaw</h1>
        </div>
      </div>

      {/* Project Selector */}
      <div className="mb-6 px-2">
        <label className="text-[10px] font-bold text-white/30 uppercase tracking-widest mb-2 block">
          Current Project
        </label>
        <div className="relative group">
          <select 
            value={selectedProjectId || ''} 
            onChange={(e) => onSelectProject(e.target.value)}
            className="w-full bg-white/5 border border-white/10 rounded-xl p-2.5 text-xs text-white/70 appearance-none cursor-pointer focus:outline-none focus:border-peixoto-primary/50 transition-colors"
          >
            <option value="" className="bg-peixoto-dark text-white/40">No Project Selected</option>
            {projects.map(p => (
              <option key={p.id} value={p.id} className="bg-peixoto-dark text-white">{p.name}</option>
            ))}
          </select>
          <Folder size={14} className="absolute right-3 top-1/2 -translate-y-1/2 text-white/20 group-hover:text-peixoto-primary transition-colors pointer-events-none" />
        </div>
      </div>

      <button 
        onClick={onNewChat}
        className="mb-6 w-full group flex items-center gap-3 p-3 rounded-xl transition-all duration-200 bg-peixoto-primary/10 border border-peixoto-primary/30 text-peixoto-primary hover:bg-peixoto-primary/20"
      >
        <Plus size={18} />
        <span className="font-semibold text-sm">New Chat</span>
      </button>

      <div className="flex-1 overflow-y-auto space-y-6 pr-2 custom-scrollbar">
        {/* Conversations History */}
        <div>
          <div className="flex items-center gap-2 text-xs font-semibold text-white/40 uppercase tracking-widest px-2 mb-3">
            <Brain size={12} />
            Chat History
          </div>
          <div className="space-y-1">
            {conversations.length === 0 ? (
              <div className="px-2 text-xs text-white/20 italic">No history yet</div>
            ) : (
              conversations.map((conv) => (
                <div key={conv.id} className="group flex items-center gap-1">
                  <button
                    onClick={() => onSelectConversation(conv.id)}
                    className={`flex-1 text-left p-2 rounded-lg text-xs truncate transition-colors ${
                      selectedConversationId === conv.id
                        ? 'bg-white/10 text-white font-medium'
                        : 'text-white/40 hover:bg-white/5 hover:text-white/60'
                    }`}
                  >
                    {new Date(conv.created_at).toLocaleDateString()} - {conv.id}
                  </button>
                  <button 
                    onClick={(e) => onDeleteConversation(conv.id, e)}
                    className="p-2 opacity-0 group-hover:opacity-100 text-white/20 hover:text-red-400 transition-all"
                  >
                    <Trash2 size={14} />
                  </button>
                </div>
              ))
            )}
          </div>
        </div>

        {/* Available Skills */}
        <div>
          <div className="flex items-center gap-2 text-xs font-semibold text-white/40 uppercase tracking-widest px-2 mb-3">
            <Code size={12} />
            Available Skills
          </div>
          
          <div className="space-y-1">
            {loading ? (
              <div className="p-4 text-white/40 text-sm animate-pulse">Loading skills...</div>
            ) : (
              skills.map((skill) => (
                <button
                  key={skill.name}
                  draggable
                  onDragStart={(e) => {
                    e.dataTransfer.setData('skillName', skill.name);
                    e.dataTransfer.effectAllowed = 'copy';
                  }}
                  onClick={() => onSelectSkill(skill.name)}
                  className={`w-full group relative flex items-center gap-3 p-2 rounded-xl transition-all duration-200 ${
                    selectedSkill === skill.name 
                      ? 'bg-peixoto-primary/20 border-peixoto-primary/30 text-white' 
                      : 'hover:bg-white/5 border-transparent text-white/60 hover:text-white'
                  } border`}
                >
                  <div className={`p-1.5 rounded-lg ${selectedSkill === skill.name ? 'bg-peixoto-primary text-white' : 'bg-white/5 text-white/40 group-hover:bg-white/10 group-hover:text-white/80'}`}>
                    <Code size={14} />
                  </div>
                  <span className="font-medium text-[13px] truncate">{skill.name}</span>
                  
                  {selectedSkill === skill.name && (
                    <Check size={12} className="ml-auto text-peixoto-primary" />
                  )}

                  {/* Hover Info Tooltip */}
                  <div className="absolute left-full ml-4 w-64 p-4 glass-panel invisible group-hover:visible opacity-0 group-hover:opacity-100 transition-all z-50 pointer-events-none scale-95 group-hover:scale-100 shadow-2xl">
                    <h4 className="font-bold text-peixoto-primary mb-1">{skill.name}</h4>
                    <p className="text-xs text-white/70 leading-relaxed">{skill.description}</p>
                  </div>
                </button>
              ))
            )}
          </div>
        </div>
      </div>

      <button 
        onClick={onInstallClick}
        className="mt-6 w-full peixoto-button flex items-center justify-center gap-2 group"
      >
        <Plus size={18} className="group-hover:rotate-90 transition-transform" />
        <span>Install Skill</span>
      </button>

      <div className="mt-6 pt-6 border-t border-white/5 flex items-center gap-3 px-2">
        <div className="w-8 h-8 rounded-full bg-peixoto-primary/20 border border-peixoto-primary/30 flex items-center justify-center text-peixoto-primary">
          BP
        </div>
        <div className="flex-1">
          <p className="text-xs font-medium text-white">Breno Peixoto</p>
          <p className="text-[10px] text-white/40">Local Station</p>
        </div>
        <Settings size={18} className="text-white/40 hover:text-white cursor-pointer" />
      </div>
    </div>
  );
};

export default Sidebar;
