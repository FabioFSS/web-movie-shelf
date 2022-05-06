import React, { useState } from "react";
import './styles.scss'
import { FaEnvelope } from "react-icons/fa";

export default function Scroll() {
    const [email, setEmail] = useState();

    return (
        <div className="wrapper-reset">
            <div className="container-reset">
                <div className="content">
                    <h1 className="pageName">Recover</h1>

                    <span className="info-reset">Enter your email to reset password</span>
                    <div className="inputContent">
                        <FaEnvelope />
                        <input className="input" type="email" placeholder="E-mail" value={email} onChange={(e) => setEmail(e.target.value)} />
                    </div>

                    <button className="button-send" disabled={!email}>
                        <a href="http://localhost:3000/login">SENDE</a>
                    </button>

                    <div>
                        <span className="span">Have you recovered your password? </span>
                        <span className="text-login">
                            <a href="http://localhost:3000/login">Log in</a>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    );
};