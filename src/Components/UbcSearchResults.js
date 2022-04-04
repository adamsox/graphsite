

export default function UbcSearchResults(props) {
    console.log(props.courses)
  
      if (props.courses !== null){
  
        return (
          <div >
            
            {props.courses.map(course => <p style = {
            {
              outline: '1px solid black',
            }
          }> <h1>{course.cc}
              </h1> {course.cred} {course.desc}</p>)}
          </div>
        );
      }else {
        return <p>no results :(</p> 
      }
    }