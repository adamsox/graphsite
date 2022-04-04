

export default function SearchResults(props) {
  console.log(props.courses)

    if (props.courses !== null){

      return (
        <div>
        {/* <p>The current data is {JSON.stringify(props.courses)}.</p> */}
          {props.courses.map(course => <p style = {
            {
              outline: '1px solid black',
              
            }
          }> <h1>{course.cc}</h1>  {course.cred} {course.desc} {course.off}</p>)}
        </div>
      );
    }else {
      return <p>no results :(</p> 
    }
  }