



export default function ImproveSkills(){
    const list = [
        "Learn new recepies",
        "Experiment with food",
        "Write your own recepies",
        "Get cooking tips",
        "Get ranked"
    ]

    const NavigateLogin = () => {
        
            window.location.href = "/Login"; 

        };
    
    return (
        <div className="section improve-skills">
            <div className="col img">
                <img src="/img/gallery/img_10.jpg" alt="" />
            </div>
            <div className="col typography">
                <h1 className="title">Improve Your Culinary Skills</h1>
                { list.map((item, index) => (
                    <p className="skill-item" key={index}>{item}</p>
                )) }
                <button className="btn" onClick={NavigateLogin}>Login  now</button>
                
               </div>
        </div>
    )
}