import { useState } from 'react'
import { generate } from '../api'
import QuizCard from './QuizCard'

export default function GenerateTab(){
  const [url, setUrl] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  async function onGenerate(){
    setLoading(true); setError(null)
    try{
      const res = await generate(url)
      setResult(res.data)
    }catch(e){
      setError(e?.response?.data?.detail || e.message)
    }finally{ setLoading(false) }
  }

  return (
    <div>
      <input style={{width:'70%',padding:8}} value={url} onChange={e=>setUrl(e.target.value)} placeholder="https://en.wikipedia.org/wiki/Alan_Turing" />
      <button onClick={onGenerate} style={{marginLeft:8}}>Generate</button>
      {loading && <div>Loading...</div>}
      {error && <div style={{color:'red'}}>{error}</div>}
      {result && <QuizCard page={result} />}
    </div>
  )
}
