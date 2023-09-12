import './Contents.css'
import Inno from './Experience/Inno/Inno'
import Workfall from './Experience/Workfall/Workfall'
import CC from './Experience/Codeclause/CC'
export default function Contents()
{
    return(
        <div className="main-container">
            <div className='General-description'>
                <h2>About</h2>
                
                <p>Bachelor’s degree in information technology specializing in AI and Data Science. Solid foundation in machine learning, natural language processing, Deep learning, and data analytics. Passionate about staying updated on the latest advancements through continuous self-learning. Actively participate in coding competitions and hackathons for practical application and collaboration. Motivated to excel in demanding digital intelligence processing environments. Skilled in the latest machine learning techniques. Strong problem-solving abilities to derive valuable insights from complex data sets. </p>
            </div>

            <div className='Professional Experience'>
            <h2>Experience</h2>
                <Inno/>
                <Workfall/>
                <CC/>
            </div>

            <div className="School-contianer">
            <h2>Education</h2>

            <p>            Bachelor of Technology-IT            • St. Joseph’s College of Engineering, Chennai          Graduation Year (2025) 
</p>
<p>            High School- Information Practices                • Sri Chaitanya Techno Schools, Bangalore                              (2021) 
</p>
<p>              Secondary Diploma Program (CCII)-C++ • Bharathiar University                              	           (2017-2018) </p>

            </div>

        </div>
    )

}