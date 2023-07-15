import {
    BrowserRouter as Router,
    Routes,
    Route
  } from "react-router-dom"
  
  import Navbar from "./components/Navbar"
  import Footer from "./components/Footer";
  
  import Home from "./pages/Home";
  import Recipes from "./pages/Recipes";
  import Login from "./pages/Login";
  import Settings from "./pages/Settings";
  import Signin from "./pages/Signin";
 import More from "./pages/More"
 import Recipedetail from "./pages/Recipedetail";

  function App() {
    return (
      <Router>
        <Navbar />
        <div className="container main">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/recipes" element={<Recipes />} />
            <Route path="/settings" element={<Settings />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signin" element={<Signin />} />
            <Route path="/more" element={<More />} />
            <Route path="/Recipedetail/:recipename" element={<Recipedetail />} />
            {/*<Route path="/Recipedetail" component={Recipedetail} />*/}
          </Routes>
        </div>
        <Footer />
      </Router>
    )
  }
  
  export default App;