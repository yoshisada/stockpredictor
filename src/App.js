import './App.css';
import React, { useState, useEffect } from "react";
import Grouped from './component/Grouped';
import { Box, Grid, Typography } from '@material-ui/core';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  //this useEffect only runs once when rendered since the array does not include any variables

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);


  /*
    Filters according to the the search value. 
    Display all users with the name and/or city that possess the substring in the search bar

    runs ONCE after initial rendering
    and after every rendering ONLY IF 'prop' or 'state' changes
  */



  // if you set state in the body of the component (or in render) you’ll have an infinite loop.
  return (
    <Box width={4 / 5} m="auto" mt={5}>
      <Grid className="App" width={4 / 5}>
        <Grid container direction="row" alignItems="center" p={5}>
          <Grid item xs={9}>
            <Typography variant="h2" style={{ display: "flex", justifyContent: "flex-start" }} >
              Stock Market Forecasting
            </Typography>
            <Typography variant="h6" style={{ display: "flex", justifyContent: "flex-start" }} >
              by: Ryan Suematsu
            </Typography>
            
          </Grid>
          <Grid item xs={3}>
            <Box>


              <img src="ssmyBlack.png" alt="logo" height="100" />
            </Box>
          </Grid>
        </Grid>
        <Grid container direction="row" alignItems="center" mt={5}>
          <Grid item xs={9}>
            <Grouped />
          </Grid>
          <Grid item xs={3}>
            <Box>
            </Box>
          </Grid>
        </Grid>
        <Grid container direction="row" alignItems="center" mt={5}>
          <Grid item xs={5}>
            <Box>


              <img src="5yr.png" alt="logo" width="100%" />
            </Box>
          </Grid>
          <Grid item xs={5}>
            <Box>


              <img src="5yrForecast.png" alt="logo" width="100%" />
            </Box>
          </Grid>
        </Grid>
      </Grid>
      <p>A small single page web application to perform some basic predictions on any single stock in the S and P 500.
        This app utilizes a React.js frontend with a Flask backend to display prediction information generated by Facebook Prophet.
        To use this app, simply search for and select a stocks ticker in the search bar, then in approximately 5 seconds the new updated
        graphs will appear.  The full code can be found here <a href='https://github.com/yoshisada/stockpredictor'>github.com/yoshisada/stockpredictor</a>
      </p>
      <p style={{fontSize: 5}}>{currentTime}</p>
    </Box>
  );
}

export default App;