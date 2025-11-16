export default function QuizCard({ page }){
  return (
    <div style={{ marginTop: 20, border: '1px solid #ddd', padding: 20 }}>
      <h2>{page.title}</h2>
      <p>{page.summary}</p>
      {page.quiz?.map((q,i)=> (
        <div key={i} style={{marginTop:12, padding:10, border:'1px solid #ccc'}}>
          <b>Q{i+1}. {q.question}</b>
          <ul>{q.options?.map((o,j)=><li key={j}>{o}</li>)}</ul>
          <p><b>Answer:</b> {q.answer}</p>
          <p><b>Difficulty:</b> {q.difficulty}</p>
          <i>{q.explanation}</i>
        </div>
      ))}
      <h3>Related Topics</h3>
      <ul>{page.related_topics?.map((t,i)=><li key={i}>{t}</li>)}</ul>
    </div>
  )
}
