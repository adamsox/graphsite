import React, { useState, useEffect } from 'react';
import './App.css';
import SearchResults from './Components/SearchResults';
import Graph from "react-graph-vis";

const axios = require('axios').default;

function randomColor() {
  const red = Math.floor(Math.random() * 256).toString(16).padStart(2, '0');
  const green = Math.floor(Math.random() * 256).toString(16).padStart(2, '0');
  const blue = Math.floor(Math.random() * 256).toString(16).padStart(2, '0');
  return `#${red}${green}${blue}`;
}

const options = {
  layout: {
    hierarchical: false
  },
  edges: {
    color: "#000000"
  }
};


function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [cc, setCC] = useState('cis');
  const [name, setName] = useState('CIS');
  const [year, setYear] = useState('');
  const [weight, setWeight] = useState('');
  const [off, setOff] = useState('');
  const [showUog, setShowUog] = useState(true);
  const [showGraph, setShowGraph] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [resultGraph, setResultGraph] = useState({
    nodes: [
      { id: 1, label: 'Node 1', color: '#ff0000' },
      { id: 2, label: 'Node 2', color: '#00ff00' },
      { id: 3, label: 'Node 3', color: '#00ff20' },

    ],
    edges: [
      { from: 1, to: 2 }
    ]
  });

  const createNode = (x, y) => {
    const color = randomColor();
    setResultGraph(({ graph: { nodes, edges }, counter, ...rest }) => {
      const id = counter + 1;
      const from = Math.floor(Math.random() * (counter - 1)) + 1;
      return {
        graph: {
          nodes: [
            ...nodes,
            { id, label: `Node ${id}`, color, x, y }
          ],
          edges: [
            ...edges,
            { from, to: id }
          ]
        },
        counter: id,
        ...rest
      }
    });
  }

  const events =  {
    select: ({ nodes, edges }) => {
      console.log("Selected nodes:");
      console.log(nodes);
      console.log("Selected edges:");
      console.log(edges);
      alert("Selected node: " + nodes);
    },
    doubleClick: ({ pointer: { canvas } }) => {
      createNode(canvas.x, canvas.y);
    }
  }

  const [course, setCourse] = useState([]);


  function handleGraphQuery(query){

        var myParams = {
        data: query
    }
  
    if (query !== "") {
        axios.post('http://131.104.49.112/api/graph', myParams)


            .then(function(response){

                console.log("Respone")
                
                console.log(response)

               setResultGraph(response.data);

                setIsLoading(false);


  
                console.log("Course")
  
       //Perform action based on response
        })
        .catch(function(error){
            console.log(error);
       //Perform action based on error
        });
    } else {
        alert("The search query cannot be empty")
    }
  }

  function handlePostQuery(query){

    var myParams = {
        data: query
    }
  
    if (query !== "") {
        axios.post('http://131.104.49.112/api/query', myParams)
            .then(async function(response){
                
                console.log("posted successfully")

                console.log(response.data)
                setCourse(response.data);
                console.log(course);
  
                console.log("Course")
  
       //Perform action based on response
        })
        .catch(function(error){
            console.log(error);
       //Perform action based on error
        });
    } else {
        alert("The search query cannot be empty")
    }
  }
    
    const handleSubmit = (e) => {
    
        e.preventDefault();

        console.log(`Form submitted, ${cc}`);

        let input = []

        if(cc === ""){
          input.push('x')
        }else {
          input.push(cc)
        }

        if(year === ""){
          input.push('x')
        }else {
          input.push(year)
        }

        if(weight === ""){
          input.push('x')
        }else {
          input.push(weight)
        }

        if(off === ""){
          input.push('x')
        }else {
          input.push(off)
        }
        
        console.log({input})
        
        handlePostQuery({input})

    }

    const handleGraphSubmit = (e) => {
      
      e.preventDefault();

      console.log(`Form submitted, ${name}`);   
      
      console.log({name})
      
      handleGraphQuery({name})
    }

    const showUogSearch = () => {
      setShowUog(true);
      setShowGraph(false);
    }

    const showGraphForm = () => {
      setShowGraph(true);
      setShowUog(false);
    }

  useEffect(() => {
    fetch('http://131.104.49.112/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App" style={{ background: "#61dafb" }}>

    {/* KEEP FOR MANUAL SERVER TESTING */}
    {/* <p style={{ background: "#61dafb" }}>The current time is {currentTime}.</p> */}
    

     <button 
     style={{margin:"10px"}}
      onClick={showUogSearch}
      className="btn btn-primary"
      >
      Search Uog Courses
      <i className="bi bi-pencil-square m-2"></i>
      </button>

      <button 
      onClick={showGraphForm}
      className="btn btn-primary"
      >
      Create Subject Graph
      <i className="bi bi-pencil-square m-2"></i>
      </button>

      <div>
      {showUog && <h1 style={{fontFamily: "Poppins"}}>
        Example input: cis x x x  
      </h1>}

      {showGraph && <h1 style={{fontFamily: "Poppins"}}>
        Example input: HIST
      </h1>}

      { showUog && <form  className="shadow p-4" onSubmit = {handleSubmit}>
            <input className="form-control" onChange = {(e) => {setCC(e.target.value)}} value = {cc}></input><br/>
            <input className="form-control" onChange = {(e) => setYear(e.target.value)} value = {year}></input><br/>
            <input className="form-control" onChange = {(e) => setWeight(e.target.value)} value = {weight}></input><br/>
            <input className="form-control" onChange = {(e) => setOff(e.target.value)} value = {off}></input><br/>

            <button className="btn btn-primary mt-2" type = 'submit'>Click to submit</button>
        </form>
      }

      {showUog && <SearchResults 
      courses={course}
      />}

      { showGraph && <form  className="shadow p-4" onSubmit = {handleGraphSubmit}>
            <input className="form-control" onChange = {(e) => {setName(e.target.value.toUpperCase())}} value = {name}></input><br/>

            <button className="btn btn-primary mt-2" type = 'submit'>Click to submit</button>
        </form>
      }

      {showGraph && (isLoading ? (<div></div>) : <div><Graph graph={resultGraph} options={options} events={events} style={{ height: "640px" }}/></div>)}

      </div>
      

    </div>
  );
}




export default App;
