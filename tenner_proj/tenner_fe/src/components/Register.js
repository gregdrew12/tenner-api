import axios from "axios";
import {useState} from "react";
import { API_URL } from "../constants";

export const Register = () => {
    
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [passwordRe, setPasswordRe] = useState('')
    const [error, setError] = useState('')

    const createUser = async e => {
        e.preventDefault();
        const user = {
            email: email,
            password: password,
            passwordRe: passwordRe
        }; 
        
        if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(email)) {
            setError('Invalid email.')
        }
        else if (password !== passwordRe) {
            setError('Passwords don\'t match.')
        }
        else if (!/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.*[a-zA-Z]).{8,}$/i.test(password)) {
            setError('Password doesn\'t meet the given requirements.')
        }
        else {
            axios.post(API_URL, user).then(res => {
                if (res.data === 'dupe') {
                    setError('There is already an account associated with this Email.')
                }
                else {
                    window.location.href = '/login';
                }
            });
        }              
    };

    return(
        <div className="Auth-form-container">
            <form className="Auth-form" onSubmit={createUser}>
                <div className="Auth-form-content">
                    <h3 className="Auth-form-title">Register</h3>
                    <h4 className="Auth-form-error">{error}</h4>
                    <div className="form-group mt-3">
                        <label>Email</label>
                        <input className="form-control mt-1" 
                            placeholder="Enter Email" 
                            name='email'  
                            type='text' value={email}
                            required 
                            onChange={e => setEmail(e.target.value)}/>
                    </div>
                    <div className="form-group mt-3">
                        <label>Password</label>
                        <input name='password' 
                            type="password"     
                            className="form-control mt-1"
                            placeholder="Choose password"
                            value={password}
                            required
                            onChange={e => setPassword(e.target.value)}/>
                        <label style={{fontSize: '13px', color: 'Gray', opacity: '75%', fontWeight: '500'}}>
                            Minimum length of 8 characters. <br/>
                            Must contain at least one upper case letter, number, and special character.<br/>
                        </label>
                    </div>
                    <div className="form-group mt-3">
                        <label>Confirm Password</label>
                        <input name='passwordRe' 
                            type="password"     
                            className="form-control mt-1"
                            placeholder="Confirm password"
                            value={passwordRe}
                            required
                            onChange={e => setPasswordRe(e.target.value)}/>
                    </div>
                    <div className="d-grid gap-2 mt-3">
                        <button type="submit" className="btn btn-primary">Submit</button>
                    </div>
                </div>
            </form>
        </div>
    )
}