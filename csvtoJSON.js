//import { print } from "util";

// Use d3 to parse csv 

<script src="https://d3js.org/d3.v5.js"></script>

var d3 = require("d3");

d3.csv("/Users/lyujinghong/Desktop/MIT/0 - 课程/2018 Spring/1.001 Engineering Computation for Data Science.001/0 - Project/Data analysis/2017_pop_trips_monthly_dropDuplicates.csv", function(data) {
    console.log(data[0]);
  });
