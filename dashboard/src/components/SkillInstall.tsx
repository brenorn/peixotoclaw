import React, { useState } from 'react';
import { Link, Download, X, AlertCircle, Loader2 } from 'lucide-react';
import axios from 'axios';
import { motion } from 'framer-motion';

interface SkillInstallProps {
  onClose: () => void;
  onSuccess: () => void;
}

const SkillInstall: React.FC<SkillInstallProps> = ({ onClose, onSuccess }) => {
  const [url, setUrl] = useState('');
  const [name, setName] = useState('');
  const [installing, setInstalling] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [auditReport, setAuditReport] = useState<string | null>(null);
  const [isRiskDetected, setIsRiskDetected] = useState(false);

  const handleInstall = async () => {
    if (!url || !name) {
      setError('Please provide both a name and a valid URL.');
      return;
    }

    setInstalling(true);
    setError(null);
    setAuditReport(null);
    setIsRiskDetected(false);

    try {
      const response = await axios.post('http://localhost:3001/api/skills/install', { url, name });
      setAuditReport(response.data.report);
      // Wait a bit to show the report before closing if success
      setTimeout(() => {
        onSuccess();
        onClose();
      }, 3000);
    } catch (err: any) {
      const resp = err.response?.data;
      if (resp?.report) {
        setAuditReport(resp.report);
        setIsRiskDetected(true);
        setError(resp.error || 'Security risk detected.');
      } else {
        setError(resp?.error || 'Failed to install skill.');
      }
    } finally {
      setInstalling(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black/60 backdrop-blur-sm z-[100] flex items-center justify-center p-4">
      <motion.div 
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        className="w-full max-w-md glass-panel p-6 shadow-peixoto-lg border-peixoto-primary/20"
      >
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-2">
            <Download className="text-peixoto-primary" size={20} />
            <h3 className="text-lg font-bold text-white">Install New Skill</h3>
          </div>
          <button onClick={onClose} className="text-white/40 hover:text-white">
            <X size={20} />
          </button>
        </div>

        <div className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-white/40 uppercase mb-2">Skill Identifier</label>
            <input 
              type="text" 
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="e.g. Data-Analyzer"
              className="w-full glass-input text-sm text-white"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-white/40 uppercase mb-2">Raw File URL (Markdown)</label>
            <div className="relative">
              <Link className="absolute left-4 top-1/2 -translate-y-1/2 text-white/30" size={16} />
              <input 
                type="text" 
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="https://raw.githubusercontent.com/.../SKILL.md"
                className="w-full glass-input !pl-12 text-sm text-white"
              />
            </div>
          </div>

          {error && (
            <div className="p-3 bg-red-500/10 border border-red-500/20 rounded-xl flex items-start gap-2 text-red-400 text-xs">
              <AlertCircle size={14} className="mt-0.5" />
              <span>{error}</span>
            </div>
          )}

          {auditReport && (
            <div className={`mt-4 p-4 rounded-xl border ${isRiskDetected ? 'bg-red-500/5 border-red-500/20' : 'bg-green-500/5 border-green-500/20'}`}>
              <div className="flex items-center gap-2 mb-2">
                <AlertCircle className={isRiskDetected ? 'text-red-400' : 'text-green-400'} size={14} />
                <span className={`text-xs font-bold uppercase ${isRiskDetected ? 'text-red-400' : 'text-green-400'}`}>
                  {isRiskDetected ? 'Audit Report: HIGH RISK' : 'Audit Report: SECURE'}
                </span>
              </div>
              <div className="max-h-40 overflow-y-auto pr-2 scrollbar-thin">
                <pre className="text-[10px] text-white/60 whitespace-pre-wrap font-mono leading-relaxed">
                  {auditReport}
                </pre>
              </div>
            </div>
          )}

          {!auditReport && (
            <div className="pt-4 flex gap-3">
              <button 
                onClick={onClose}
                className="flex-1 py-2 rounded-xl bg-white/5 border border-white/10 text-white/60 hover:text-white hover:bg-white/10 transition-all font-medium text-sm"
              >
                Cancel
              </button>
              <button 
                onClick={handleInstall}
                disabled={installing}
                className="flex-[2] peixoto-button flex items-center justify-center gap-2 relative overflow-hidden"
              >
                {installing ? (
                  <>
                    <Loader2 size={18} className="animate-spin" />
                    <span>Analyzing & Auditing...</span>
                  </>
                ) : (
                  <>
                    <Download size={18} />
                    <span>Download & Install</span>
                  </>
                )}
              </button>
            </div>
          )}

          {auditReport && isRiskDetected && (
            <div className="pt-4">
              <button 
                onClick={onClose}
                className="w-full py-2 rounded-xl bg-white/5 border border-white/10 text-white/60 hover:text-white hover:bg-white/10 transition-all font-medium text-sm"
              >
                Dismiss
              </button>
            </div>
          )}
        </div>
      </motion.div>
    </div>
  );
};

export default SkillInstall;
