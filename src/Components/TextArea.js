import React,{ useState } from 'react';


const TempForm = (props) => {
    const [test, setText] = useState('')
    const [disp, setDisp] = useState('')
    // const test = ""

    const handleSubmit2=(event)=>{ 
      event.preventDefault()
      setDisp(test)
      setText('')
    }

  return (
    <div className="shadow p-4">

        <p> {disp} </p>

        <form onSubmit = {handleSubmit2} >

          <label htmlFor="title" className="form-label">Enter Text</label>
          <input 
          type="text"
          className="form-control" 
          placeholder ="Enter title"
          value={test}
          onChange={(e)=>setText(e.target.value)}
          required
          />

          <button 
          className="btn btn-primary mt-2"
          >
          Submit</button>
          
        </form>

    </div>
  )}

export default TempForm;