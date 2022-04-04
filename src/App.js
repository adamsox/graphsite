import React, { useState, useEffect } from "react";
import "./App.css";
import SearchResults from "./Components/SearchResults";
import UbcSearchResults from "./Components/UbcSearchResults";
import Graph from "react-graph-vis";

const axios = require("axios").default;

function randomColor() {
  const red = Math.floor(Math.random() * 256)
    .toString(16)
    .padStart(2, "0");
  const green = Math.floor(Math.random() * 256)
    .toString(16)
    .padStart(2, "0");
  const blue = Math.floor(Math.random() * 256)
    .toString(16)
    .padStart(2, "0");
  return `#${red}${green}${blue}`;
}

const empty_graph = {
  nodes: [],
  edges: [],
};

const options = {
  layout: {
    improvedLayout: true,
    hierarchical: {
      enabled: true,
      nodeSpacing: 10,
      treeSpacing: 10,
      direction: "UD",
      edgeMinimization: false,
      levelSeparation: 120,
      blockShifting: false,
      sortMethod: "directed",
      shakeTowards: "leaves",
    },
  },

  interaction: {
    dragNodes: true,
    dragView: true,
    hideEdgesOnDrag: false,
    hideEdgesOnZoom: false,
    hideNodesOnDrag: false,
    hover: true,
    hoverConnectedEdges: true,
    keyboard: {
      enabled: false,
      speed: { x: 10, y: 10, zoom: 0.02 },
      bindToWindow: true,
      autoFocus: true,
    },
    multiselect: false,
    navigationButtons: false,
    selectable: true,
    selectConnectedEdges: true,
    tooltipDelay: 300,
    zoomSpeed: 1,
    zoomView: true,
  },

  edges: {
    color: "#000000",
  },
};

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [name, setName] = useState("CIS");
  const [cc, setCC] = useState("");
  const [year, setYear] = useState("");
  const [weight, setWeight] = useState("");
  const [off, setOff] = useState("");
  const [ubcCC, setUbcCC] = useState("");
  const [ubcYear, setUbcYear] = useState("");
  const [ubcWeight, setUbcWeight] = useState("");
  const [showUog, setShowUog] = useState(true);
  const [showUbc, setShowUbc] = useState(false);
  const [showGraph, setShowGraph] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [resultGraph, setResultGraph] = useState({
    nodes: [
      { id: 1, label: "Node 1", color: "#ff0000" },
      { id: 2, label: "Node 2", color: "#00ff00" },
      { id: 3, label: "Node 3", color: "#00ff20" },
    ],
    edges: [{ from: 1, to: 2 }],
  });

  let updateGraph = {};
  const [resetGraph, setResetGraph] = useState({});

  const events = {
    select: ({ nodes, edges }) => {
      dropCourse(nodes[0]);
    },
    doubleClick: () => {},
  };

  function dropCourse(course) {
    console.log("RESET GRAPH: ");
    console.log(resetGraph);
    updateGraph = structuredClone(resetGraph);

    let connected = [];

    let affected = [];

    for (let i = 0; i < updateGraph.nodes.length; i++) {
      if (updateGraph.nodes[i].id === course) {
        updateGraph.nodes[i].color = "#FF0000";
        connected.push(updateGraph.nodes[i].id);
        affected.push(updateGraph.nodes[i].id);
      }
    }

    while (connected.length !== 0) {
      for (let i = 0; i < updateGraph.edges.length; i++) {
        if (
          updateGraph.edges[i].from === connected[0] &&
          updateGraph.edges[i].to.includes("*")
        ) {
          connected.push(updateGraph.edges[i].to);
          affected.push(updateGraph.edges[i].to);
        }
      }
      connected.shift();
    }

    console.log(affected);

    for (let i = 0; i < affected.length; i++) {
      for (let j = 0; j < updateGraph.nodes.length; j++) {
        if (affected[i] === updateGraph.nodes[j].id) {
          updateGraph.nodes[j].color = "#FF0000";
        }
      }
    }

    setResultGraph(empty_graph);
    setResultGraph(updateGraph);
    console.log(updateGraph);
  }

  const [course, setCourse] = useState([]);
  const [ubcCourse, setUbcCourse] = useState([]);

  function handleGraphQuery(query) {
    var myParams = {
      data: query,
    };

    if (query !== "") {
      axios
        .post("http://131.104.49.112/api/graph", myParams)

        .then(function (response) {
          // console.log("posted successfully")

          console.log("Respone");

          console.log(response);
          // setCourse(JSON.stringify(response.data));
          setResultGraph(empty_graph);

          setResultGraph(response.data);

          setResetGraph(empty_graph);
          setResetGraph(response.data);
          // setState({
          // graph: response.data,

          // })
          setIsLoading(false);
          // console.log(JSON.stringify({ x: 5, y: 6 }));

          console.log("Course");

          //Perform action based on response
        })
        .catch(function (error) {
          console.log(error);
          //Perform action based on error
        });
    } else {
      alert("The search query cannot be empty");
    }
  }

  function handleUbcPost(query) {
    var myParams = {
      data: query,
    };

    if (query !== "") {
      axios
        .post("http://131.104.49.112/api/ubc-search", myParams)
        .then(async function (response) {
          console.log("posted successfully");

          console.log(response.data);
          setUbcCourse(response.data);
          console.log(ubcCourse);
          // console.log(JSON.stringify({ x: 5, y: 6 }));

          console.log("Course");

          //Perform action based on response
        })
        .catch(function (error) {
          console.log(error);
          //Perform action based on error
        });
    } else {
      alert("The search query cannot be empty");
    }
  }

  function handlePostQuery(query) {
    var myParams = {
      data: query,
    };

    if (query !== "") {
      axios
        .post("https://131.104.49.112/api/query", myParams)
        .then(async function (response) {
          console.log("posted successfully");

          console.log(response.data);
          setCourse(response.data);
          console.log(course);
          // console.log(JSON.stringify({ x: 5, y: 6 }));

          console.log("Course");

          //Perform action based on response
        })
        .catch(function (error) {
          console.log(error);
          //Perform action based on error
        });
    } else {
      alert("The search query cannot be empty");
    }
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log(`Form submitted, ${cc}`);

    let input = [];

    if (cc === "") {
      input.push("x");
    } else {
      input.push(cc);
    }

    if (year === "") {
      input.push("x");
    } else {
      input.push(year);
    }

    if (weight === "") {
      input.push("x");
    } else {
      input.push(weight);
    }

    if (off === "") {
      input.push("x");
    } else {
      input.push(off);
    }

    console.log({ input });

    handlePostQuery({ input });
  };

  const handleUbcSubmit = (e) => {
    e.preventDefault();

    console.log(`Form submitted, ${cc}`);

    let input = [];

    if (ubcCC === "") {
      input.push("x");
    } else {
      input.push(ubcCC);
    }

    if (ubcYear === "") {
      input.push("x");
    } else {
      input.push(ubcYear);
    }

    if (ubcWeight === "") {
      input.push("x");
    } else {
      input.push(ubcWeight);
    }

    console.log({ input });

    handleUbcPost({ input });
  };

  const handleGraphSubmit = (e) => {
    e.preventDefault();

    console.log(`Form submitted, ${name}`);

    console.log({ name });

    handleGraphQuery({ name });
  };

  const showUogSearch = () => {
    setShowUog(true);
    setShowGraph(false);
    setShowUbc(false);
  };

  const showUbcSearch = () => {
    setShowUog(false);
    setShowGraph(false);
    setShowUbc(true);
  };

  const showGraphForm = () => {
    setShowGraph(true);
    setShowUog(false);
    setShowUbc(false);
  };

  useEffect(() => {
    fetch("https://131.104.49.112/api/time")
      .then((res) => res.json())
      .then((data) => {
        setCurrentTime(data.time);
      });
  }, []);

  return (
    <div className="App" style={{ background: "#78dbff" }}>
      {/* <p style={{ background: "#61dafb" }}>The current time is {currentTime}.</p> */}

      <button
        style={{ margin: "10px" }}
        onClick={showUogSearch}
        className="btn btn-primary"
      >
        Search Uog Courses
        <i className="bi bi-pencil-square m-2"></i>
      </button>

      <button onClick={showGraphForm} className="btn btn-primary">
        Create Subject Graph
        <i className="bi bi-pencil-square m-2"></i>
      </button>

      <button
        style={{ margin: "10px" }}
        onClick={showUbcSearch}
        className="btn btn-primary"
      >
        Search UBC Courses
        <i className="bi bi-pencil-square m-2"></i>
      </button>

      <div>
        {showUog}

        {showGraph}

        {showUbc}

        {showUog && (
          <form
            style={{
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
            className="shadow p-4"
            onSubmit={handleSubmit}
          >
            <input
              style={{
                width: "50%",
              }}
              className="form-control"
              placeholder="cis"
              onChange={(e) => {
                setCC(e.target.value);
              }}
              value={cc}
            ></input>
            <br />
            <input
              style={{
                width: "50%",
              }}
              className="form-control"
              placeholder="3"
              onChange={(e) => setYear(e.target.value)}
              value={year}
            ></input>{" "}
            <br />
            <input
              style={{
                width: "50%",
              }}
              className="form-control"
              placeholder="0.75"
              onChange={(e) => setWeight(e.target.value)}
              value={weight}
            ></input>
            <br />
            <input
              style={{
                width: "50%",
              }}
              className="form-control"
              placeholder="f"
              onChange={(e) => setOff(e.target.value)}
              value={off}
            ></input>
            <br />
            <button className="btn btn-primary mt-2" type="submit">
              Click to submit
            </button>
          </form>
        )}

        {showUog && <SearchResults courses={course} />}

        {showUbc && (
          <form
            style={{
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
            className="shadow p-4"
            onSubmit={handleUbcSubmit}
          >
            <input
              style={{
                width: "50%",
              }}
              className="form-control"
              placeholder="cpen"
              onChange={(e) => {
                setUbcCC(e.target.value);
              }}
              value={ubcCC}
            ></input>
            <br />
            <input
              style={{
                width: "50%",
              }}
              className="form-control"
              placeholder="4"
              onChange={(e) => setUbcYear(e.target.value)}
              value={ubcYear}
            ></input>
            <br />
            <input
              style={{
                width: "50%",
              }}
              className="form-control"
              placeholder="3"
              onChange={(e) => setUbcWeight(e.target.value)}
              value={ubcWeight}
            ></input>
            <br />

            <button className="btn btn-primary mt-2" type="submit">
              Click to submit
            </button>
          </form>
        )}

        {showUbc && <UbcSearchResults courses={ubcCourse} />}

        {showGraph && (
          <form
            style={{
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
            className="shadow p-4"
            onSubmit={handleGraphSubmit}
          >
            <input
              style={{
                width: "50%",
              }}
              className="form-control"
              onChange={(e) => {
                setName(e.target.value.toUpperCase());
              }}
              value={name}
            ></input>
            <br />

            <button className="btn btn-primary mt-2" type="submit">
              Click to submit
            </button>
          </form>
        )}

        {showGraph &&
          (isLoading ? (
            <div></div>
          ) : (
            <div>
              <Graph
                graph={resultGraph}
                options={options}
                events={events}
                style={{ height: "640px" }}
              />
            </div>
          ))}
      </div>
    </div>
  );
}

export default App;
