import { useState } from 'react'
import GenerateTab from './components/GenerateTab'
import HistoryTab from './components/HistoryTab'

export default function App(){
  const [tab, setTab] = useState('generate')
  return (
    <div style={{ padding: 20 }}>
      <h1>AI Wiki Quiz Generator</h1>
      <div style={{ marginBottom: 20 }}>
        <button onClick={()=>setTab('generate')}>Generate Quiz</button>
        <button onClick={()=>setTab('history')} style={{ marginLeft: 10 }}>History</button>
      </div>
      {tab === 'generate' ? <GenerateTab /> : <HistoryTab />}
    </div>
  )
}
