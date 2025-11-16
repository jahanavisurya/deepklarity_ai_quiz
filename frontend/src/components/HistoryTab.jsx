import { useEffect, useState } from 'react'
import { history, getQuiz } from '../api'

export default function HistoryTab(){
  const [list, setList] = useState([])
  const [selected, setSelected] = useState(null)

  useEffect(()=>{ load() }, [])

  async function load(){
    const r = await history()
    setList(r.data)
  }

  async function onDetails(id){
    const r = await getQuiz(id)
    setSelected(r.data)
  }

  return (
    <div>
      <table border="1" cellPadding="8">
        <thead><tr><th>ID</th><th>Title</th><th>URL</th><th>Action</th></tr></thead>
        <tbody>
          {list.map(item=>(
            <tr key={item.id}><td>{item.id}</td><td>{item.title}</td><td>{item.url}</td><td><button onClick={()=>onDetails(item.id)}>Details</button></td></tr>
          ))}
        </tbody>
      </table>
      {selected && <pre style={{whiteSpace:'pre-wrap', marginTop:20}}>{JSON.stringify(selected,null,2)}</pre>}
    </div>
  )
}
