import React, { useCallback } from "react";
import Particles from "react-particles";
import type { Engine } from "tsparticles-engine";
import { loadFull } from "tsparticles";
import './App.css';
import particlesOptions from "./particles.json";
import { ISourceOptions } from "tsparticles-engine";
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from "./NavBar";
import Player from "./Player";
import Footer from "./Footer";

function App() {
    
    const particlesInit = useCallback(async (engine: Engine) => {
        await loadFull(engine);
    }, []);

    return (
        
        <div className="App">
            <NavBar></NavBar>
            <Particles options={particlesOptions as ISourceOptions} init={particlesInit}/>
            <header className="App-header">
                <p>
                    <Player></Player>
                </p>

                <h2>Cosmic Reef</h2>
                <p>This science visualization presents the dramatic landscape of two nebulas in the Large Magellanic Cloud.<br />
The visualization is an interpretation of the nebulas' complex structure and is based on images by NASA's Hubble Space Telescope.</p>

            </header>
            <Footer></Footer>
        </div>
    );
}

export default App;
