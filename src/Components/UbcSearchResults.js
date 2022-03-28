

export default function UbcSearchResults(props) {
    console.log(props.courses)
  
      if (props.courses !== null){
  
        return (
          <div>
          {/* <p>The current data is {JSON.stringify(props.courses)}.</p> */}
            {props.courses.map(course => <p> {course.cc} {course.cred} {course.desc}</p>)}
          </div>
        );
      }else {
        return <p>no results :(</p> 
      }
    }