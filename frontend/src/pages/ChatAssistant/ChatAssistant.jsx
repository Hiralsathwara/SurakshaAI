import {
    useEffect,
    useRef,
    useState
} from "react";
import { useNavigate } from "react-router-dom";


import {
    FaPaperPlane,
    FaRobot,
    FaUser,
    FaMicrophone
} from "react-icons/fa";


import ReactMarkdown from "react-markdown";


import {
    sendMessage
} from "../../api/chatbotApi";


import "./ChatAssistant.css";



/*
===========================================================
        Constants
===========================================================
*/


const STORAGE_KEY = "suraksha_chat_history";



const INITIAL_MESSAGE = {

    sender:"ai",

    text:
    " Hello! I'm SurakshaAI. Ask me about scams."

};



const SUGGESTIONS = [

    "Someone asked my OTP",

    "Should I click this link?",

    "Is this UPI payment safe?"

];





function ChatAssistant(){

const navigate = useNavigate();




/*
===========================================================
        States
===========================================================
*/


const [messages,setMessages] = useState(()=>{


    const saved =
    localStorage.getItem(
        STORAGE_KEY
    );


    return saved
    ?
    JSON.parse(saved)
    :
    [
        INITIAL_MESSAGE
    ];

});



const [input,setInput] = useState("");

const [loading,setLoading] = useState(false);

const [listening,setListening] = useState(false);



const bottomRef = useRef(null);




/*
===========================================================
        Scroll Chat
===========================================================
*/


useEffect(()=>{


    bottomRef.current?.scrollIntoView({

        behavior:"smooth"

    });


},[messages]);



/*
===========================================================
        Save Chat History
===========================================================
*/


useEffect(()=>{


    localStorage.setItem(

        STORAGE_KEY,

        JSON.stringify(messages)

    );


},[messages]);


/*
===========================================================
        Send Message
===========================================================
*/


const handleSend = async()=>{


    if(!input.trim())

        return;

    const userText = input;



    setMessages(prev=>[

        ...prev,

        {
            sender:"user",
            text:userText
        }

    ]);


    setInput("");

    setLoading(true);

    try{

        const response =
        await sendMessage(
            userText
        );

        setMessages(prev=>[

            ...prev,

            {
                sender:"ai",

                text:
                response.reply

            }

        ]);



    }


    catch(error){


        console.error(error);



        setMessages(prev=>[

            ...prev,

            {

                sender:"ai",

                text:
                "Unable to connect to AI server."

            }

        ]);

    }


    finally{

        setLoading(false);

    }


};







/*
===========================================================
        Voice Input
===========================================================
*/


const startVoiceInput = ()=>{


const SpeechRecognition =
window.SpeechRecognition ||
window.webkitSpeechRecognition;



if(!SpeechRecognition){


    alert(
        "Voice input not supported"
    );


    return;

}



const recognition =
new SpeechRecognition();



recognition.lang ="en-IN";

recognition.start();

setListening(true);

recognition.onresult=(event)=>{

    const voiceText =
    event.results[0][0].transcript;

    setInput(voiceText);

    setListening(false);

};

recognition.onerror=()=>{

    setListening(false);


};

};

/*
===========================================================
        Clear Chat
===========================================================
*/


const clearChat = ()=>{


    localStorage.removeItem(
        STORAGE_KEY
    );


    setMessages([
        INITIAL_MESSAGE
    ]);

};


return(

<div className="chat-page">

<div className="chat-container">


{/* HEADER */}

<div className="chat-header">


<div className="header-title">


<FaRobot/>
        <h2>
        SurakshaAI Assistant
        </h2>
</div>
 <button
    className="page-back-button"
    onClick={() => navigate("/dashboard")}
  >
    ← Back
  </button>


<button
        className="clear-btn"
        onClick={clearChat}
>Clear Chat</button>

</div>

{/* SUGGESTIONS */}


<div className="suggestions">
<p>
Try asking:
</p>

<div className="suggestion-actions">
{SUGGESTIONS.map((item,index)=>(

<button

key={index}

type="button"

onClick={()=>setInput(item)}

>{item} </button>


))}
</div>
</div>


{/* CHAT BODY */}

<div className="chat-body">


{
messages.map(
(msg,index)=>(

<div
key={index}
className={
`message ${msg.sender}`
}

>
<div className="avatar">
{msg.sender==="user"?   <FaUser/> : <FaRobot/>}
</div>


<div className="bubble">
<ReactMarkdown>
{msg.text}
</ReactMarkdown>


</div>
</div>

))  }

{

loading &&

<div className="message ai">
<div className="avatar">

<FaRobot/>
</div>


<div className="bubble typing">

<span></span>

<span></span>

<span></span>


</div>
</div>  }

<div ref={bottomRef}/>
</div>


{/* FOOTER */}



<div className="chat-footer">

<input  type="text" placeholder="Ask about scams..."    value={input}

onChange={
(e)=>setInput(e.target.value)
}

onKeyDown={
(e)=>{

if(e.key==="Enter")

handleSend();

}
}

/>





<button

onClick={handleSend}    >

<FaPaperPlane/>
</button>

<button

className={
listening
?
"voice-btn active"
:
"voice-btn"
}

onClick={startVoiceInput}

>


<FaMicrophone/>


</button>



</div>







</div>


</div>


);


}



export default ChatAssistant;   
