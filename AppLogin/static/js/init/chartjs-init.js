( function ( $ ) {
    "use strict";

    // Team chart
    var ctx = document.getElementById( "team-chart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                data: [ 0,2543662, 2297291, 1954521, 2419252, 1090607, 2797452, 4744689, 2922748 ],
                label: "Ingresos",
                backgroundColor: 'rgba(146,1,80,0.27)',
                borderColor: 'rgba(146,1,80,0.27)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(146,1,80,0.27)',
                    }, 
                    {
                data: [ 0, 2144820, 2068431, 1959303, 2106626, 1686484, 2226666, 2837781, 2264876 ],
                label: "Costo total",
                backgroundColor: 'rgba(0,198,246,0.31)',
                borderColor: 'rgba(0,198,246,0.31)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(0,198,246,0.31)',
                    }, ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
                
            },
            legend: {
                display: false,
                position: 'top',
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                }


            },
            scales: {
                xAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Año'
                    }
                        } ],
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: true
                    },
                    ticks: { 
                        beginAtZero: true, 
                        callback: function(value, index, values) { 
                         if(parseInt(value) >= 1000){ 
                         return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "."); 
                         } else { 
                         return value; 
                         } 
                        } 
                        },
                    scaleLabel: {
                        display: true,
                        labelString: 'Bs'
                    }
                        } ]
            },
            
            title: {
                display: false,
            }
        }
    } ); 


    //Sales chart
    var ctx = document.getElementById( "sales-chart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "2010", "2011", "2012", "2013", "2014", "2015", "2016","2017","2018" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                label: "Quinua",
                data: [ 6087, 6430, 6825, 7240, 8432, 8300, 8473,9350,9123 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(220,53,69,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(220,53,69,0.75)',
                    }, {
                label: "Cebada",
                data: [ 14265, 14432, 14631, 14601, 21066, 16259, 17755,17939,19069 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(40,167,69,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(40,167,69,0.75)',
                    },{
                label: "Cañahua",
                data: [ 448, 444, 454, 481, 437, 447, 475,461,463 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(183,93,32,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(183,93,32,0.75)',
                            }  ]
        },
        options: {
            responsive: true,

            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
            },
            legend: {
                display: true,
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                },
            },
            scales: {
                xAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Month'
                    }
                        } ],
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: false
                    },
                    ticks: { 
                        beginAtZero: true, 
                        callback: function(value, index, values) { 
                         if(parseInt(value) >= 1000){ 
                         return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "."); 
                         } else { 
                         return value; 
                         } 
                        } 
                        },
                    scaleLabel: {
                        display: true,
                        labelString: 'Toneladas metricas'
                    }
                        } ]
            },
            title: {
                display: false,
                text: 'Normal Legend'
            }
        }
    } );







    //line chart
    var ctx = document.getElementById( "lineChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "Aroma", "Bautista Saavedra", "Camacho", "Gualberto Villaroel", "Ingavi", "Inquisivi", "José Manuel Pando","Los Andes","Muñecas","Murillo","Omasuyos","Pacajes" ],
            datasets: [
                {
                    label: "Quinua",
                    borderColor: "rgba(275,95,42,0.9)",
                    borderWidth: "1",
                    backgroundColor: "rgba(275,95,42,0.1)",
                    data: [ 5665, 10, 30, 2105, 859, 49, 27,905,0,40,294,1130 ]
                            },
                {
                    label: "Cebada",
                    borderColor: "rgba(0, 194, 146, 0.3)",
                    borderWidth: "1",
                    backgroundColor: "rgba(74,99,129,0.3)",
                    pointHighlightStroke: "rgba(26,179,148,1)",
                    data: [ 6232, 66, 437, 3331, 2998, 467,167,1458,72,281,658,4351 ]
                            },
                {
                    label: "Cañahua",
                    borderColor: "rgba(74,99,129,0.3)",
                    borderWidth: "1",
                    backgroundColor: "rgba(74,99,129,1)",
                    pointHighlightStroke: "rgba(26,179,148,1)",
                    data: [ 11, 3, 4, 215, 131, 27, 8,7,0,0,8,211 ]
                            }
                        ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                intersect: false
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: false
                    },
                    ticks: { 
                        beginAtZero: true, 
                        callback: function(value, index, values) { 
                         if(parseInt(value) >= 1000){ 
                         return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "."); 
                         } else { 
                         return value; 
                         } 
                        } 
                        },
                    scaleLabel: {
                        display: true,
                        labelString: 'Toneladas metricas'
                    }
                        } ]
            }
        }
    } );


    

    //bar chart
    var ctx = document.getElementById( "barChart" );
    //    ctx.height = 200;
    var myChart = new Chart( ctx, {
        type: 'bar',
        data: {
            labels: [ "2020", "2021", "2022", "2023", "2024", "2025", "2026","2027","2028","2029","2030" ],
            datasets: [
                {
                    label: "Demanda",
                    data: [ 1297, 1304, 1306, 1307, 1314, 1308, 1324, 1320, 1332,1349,1364 ],
                    borderColor: "rgba(255,123,77)",
                    borderWidth: "0",
                    backgroundColor: "rgba(255,123,77,0.7)"
                            },
                {
                    label: "Oferta",
                    data: [ 1283, 1286, 1290, 1293, 1297, 1301, 1304 , 1308, 1311,1315,1318 ],
                    borderColor: "rgba(103,163,171)",
                    borderWidth: "0",
                    backgroundColor: "rgba(103,163,171,0.7)"
                            }
                
                        ]
        },
        options: {
            scales: {
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: false
                    },
                    ticks: { 
                        beginAtZero: true, 
                        min: 1200,
                        max: 1400,
                        stepSize: 20,
                        callback: function(value, index, values) { 
                         if(parseInt(value) >= 1000){ 
                         return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "."); 
                         } else { 
                         return value; 
                         } 
                        } 
                        },
                    scaleLabel: {
                        display: true,
                        labelString: 'Toneladas metricas'
                    }
                                } ]
            }
        }
    } );

    //radar chart
    var ctx = document.getElementById( "radarChart" );
    ctx.height = 160;
    var myChart = new Chart( ctx, {
        type: 'radar',
        data: {
            labels: ["Fibra","Proteina","Humedad" ,"Grasa" ],
            datasets: [
                {
                    label: "Quinua",
                    data: [ 7.0, 14.12,13.28,6.7 ],
                    borderColor: "rgba(143,22,17,1)",
                    borderWidth: "1",
                    backgroundColor: "rgba(143,22,17,0.29)"
                            },
                {
                    label: "Cebada",
                    data: [  17.3, 12.48, 9.44,2.30],
                    borderColor: "rgba(192,83,17,1)",
                    borderWidth: "1",
                    backgroundColor: "rgba(192,83,17,0.29)"
                            },
                {
                    label: "Cañahua",
                    data: [ 9.8,14, 7.7,4.5],
                    borderColor: "rgba(134,123,107,1)",
                    borderWidth: "1",
                    backgroundColor: "rgba(134,123,107,0.37)"
                            }
                        ]
        },
        options: {
            legend: {
                position: 'top'
            },
            scale: {
                ticks: {
                    beginAtZero: true
                }
            }
        }
    });

    //pie chart
    var ctx = document.getElementById( "pieChart" );
    ctx.height = 100;
    var dat = document.getElementById("misdatos").textContent;
    var daat1 = dat.split('[');
    var daat2 = daat1[1].split(']');
    var datoos = daat2[0].split(',');
    var myChart = new Chart( ctx, {
        type: 'pie',
        data: {
            datasets: [ {
                data: [ datoos[0], datoos[1], datoos[2],datoos[3], datoos[4] ],
                backgroundColor: [
                                    "rgba(97,65,34,0.8)",
                                    "rgba(233,83,0,0.8)",
                                    "rgba(255,0,0,0.8)",
                                    "rgba(255,188,65,0.8)",
                                    "rgba(220,123,107,0.8)",
                                    
                                ],
                hoverBackgroundColor: [
                                    "rgba(97,65,34)",
                                    "rgba(233,83,0)",
                                    "rgba(255,0,0)",
                                    "rgba(255,188,65)",
                                    "rgba(220,123,107)",
                                    
                                ]

                            } ],
            labels: [
                            "Chocolate",
                            "Naranja",
                            "Frutilla",
                            "Vainilla",
                            "Original"
                        ]
        },
        options: {
            responsive: true
        }
    } );

    

    //doughut chart
    var ctx = document.getElementById( "doughutChart" );
    ctx.height = 100;
    var myChart = new Chart( ctx, {
        type: 'doughnut',
        data: {
            datasets: [ {
                data: [ 35, 27, 16,9,13 ],
                backgroundColor: [
                                    "rgba(0, 94, 46,0.9)",
                                    "rgba(30, 154, 37,0.7)",
                                    "rgba(3,164,146)",
                                    "rgba(3,189,255)",
                                    "rgba(0,20,50,0.7)"
                                ],
                hoverBackgroundColor: [
                                    "rgba(0, 94, 46,0.9)",
                                    "rgba(30, 154, 37,0.7)",
                                    "rgba(3,164,146)",
                                    "rgba(3,189,255)",
                                    "rgba(0,20,50,0.7)"
                                ]

                            } ],
            labels: [
                            "Kellogg's",
                            "Nestle",
                            "Princesa",
                            "KRIS",
                            "Otros"
                        ]
        },
        options: {
            responsive: true
        }
    } );

    

    // single bar chart 
    var ctx = document.getElementById( "singelBarChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'bar',
        data: {
            labels: [ "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54","55-59","60-64" ],
            datasets: [
                {
                    label: "Población por edades",
                    data: [ 247310, 224066, 212115, 202653, 182634, 158280, 135738,114086,95064 ],
                    borderColor: "rgba(74,99,129,1)",
                    borderWidth: "0",
                    backgroundColor: "rgba(74,99,129,1)"
                            }
                        ]
        },
        options: {
            scales: {
                yAxes: [ {
                    ticks: { 
                        beginAtZero: true, 
                        
                        callback: function(value, index, values) { 
                         if(parseInt(value) >= 1000){ 
                         return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "."); 
                         } else { 
                         return value; 
                         } 
                        } 
                        }
                                } ]
            }
        }
    } );

     //line chart 2
     var ctx = document.getElementById( "Chartline" );
     ctx.height = 150;
     var myChart = new Chart( ctx, {
         type: 'line',
         data: {
             labels: [ "Aroma", "Bautista Saavedra", "Camacho", "Gualberto Villaroel", "Ingavi", "Inquisivi", "José Manuel Pando","Los Andes","Muñecas","Murillo","Omasuyos","Pacajes" ],
             datasets: [
                 {
                     label: "Quinua",
                     borderColor: "rgba(275,95,42,0.9)",
                     borderWidth: "1",
                     backgroundColor: "rgba(275,95,42,0.1)",
                     data: [ 5665, 10, 30, 2105, 859, 49, 27,905,0,40,294,1130 ]
                             },
                 {
                     label: "Cebada",
                     borderColor: "rgba(0, 194, 146, 0.3)",
                     borderWidth: "1",
                     backgroundColor: "rgba(74,99,129,0.3)",
                     pointHighlightStroke: "rgba(26,179,148,1)",
                     data: [ 6232, 66, 437, 3331, 2998, 467,167,1458,72,281,658,4351 ]
                             },
                 {
                     label: "Cañahua",
                     borderColor: "rgba(74,99,129,0.3)",
                     borderWidth: "1",
                     backgroundColor: "rgba(74,99,129,1)",
                     pointHighlightStroke: "rgba(26,179,148,1)",
                     data: [ 11, 3, 4, 215, 131, 27, 8,7,0,0,8,211 ]
                             }
                         ]
         },
         options: {
             responsive: true,
             tooltips: {
                 mode: 'index',
                 intersect: false
             },
             hover: {
                 mode: 'nearest',
                 intersect: true
             },
             scales: {
                 yAxes: [ {
                     display: true,
                     gridLines: {
                         display: true,
                         drawBorder: false
                     },
                     ticks: { 
                         beginAtZero: true, 
                         callback: function(value, index, values) { 
                          if(parseInt(value) >= 1000){ 
                          return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "."); 
                          } else { 
                          return value; 
                          } 
                         } 
                         },
                     scaleLabel: {
                         display: true,
                         labelString: 'Toneladas metricas'
                     }
                         } ]
             }
         }
     } );


     // Team chart111111
    var ctx = document.getElementById("cha-team");
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                data: [ 0,2543662, 2297291, 1954521, 2419252, 1090607, 2797452, 4744689, 2922748 ],
                label: "Ingresos",
                backgroundColor: 'rgba(146,1,80,0.27)',
                borderColor: 'rgba(146,1,80,0.27)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(146,1,80,0.27)',
                    }, 
                    {
                data: [ 0, 2144820, 2068431, 1959303, 2106626, 1686484, 2226666, 2837781, 2264876 ],
                label: "Costo total",
                backgroundColor: 'rgba(0,198,246,0.31)',
                borderColor: 'rgba(0,198,246,0.31)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(0,198,246,0.31)',
                    }, ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
                
            },
            legend: {
                display: false,
                position: 'top',
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                }


            },
            scales: {
                xAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Año'
                    }
                        } ],
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: true
                    },
                    ticks: { 
                        beginAtZero: true, 
                        callback: function(value, index, values) { 
                         if(parseInt(value) >= 1000){ 
                         return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "."); 
                         } else { 
                         return value; 
                         } 
                        } 
                        },
                    scaleLabel: {
                        display: true,
                        labelString: 'Bs'
                    }
                        } ]
            },
            
            title: {
                display: false,
            }
        }
    } ); 
    

        // Team chart2222
    var ctx = document.getElementById( "dos" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                data: [ 0,2543662, 2297291, 1954521, 2419252, 1090607, 2797452, 4744689, 2922748 ],
                label: "Ingresos",
                backgroundColor: 'rgba(146,1,80,0.27)',
                borderColor: 'rgba(146,1,80,0.27)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(146,1,80,0.27)',
                    }, 
                    {
                data: [ 0, 2144820, 2068431, 1959303, 2106626, 1686484, 2226666, 2837781, 2264876 ],
                label: "Costo total",
                backgroundColor: 'rgba(0,198,246,0.31)',
                borderColor: 'rgba(0,198,246,0.31)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(0,198,246,0.31)',
                    }, ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
                
            },
            legend: {
                display: false,
                position: 'top',
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                }


            },
            scales: {
                xAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Año'
                    }
                        } ],
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: true
                    },
                    ticks: { 
                        beginAtZero: true, 
                        callback: function(value, index, values) { 
                         if(parseInt(value) >= 1000){ 
                         return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "."); 
                         } else { 
                         return value; 
                         } 
                        } 
                        },
                    scaleLabel: {
                        display: true,
                        labelString: 'Bs'
                    }
                        } ]
            },
            
            title: {
                display: false,
            }
        }
    } ); 


    // Team chart3333
    var ctx = document.getElementById( "tres" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                data: [ 0,2543662, 2297291, 1954521, 2419252, 1090607, 2797452, 4744689, 2922748 ],
                label: "Ingresos",
                backgroundColor: 'rgba(146,1,80,0.27)',
                borderColor: 'rgba(146,1,80,0.27)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(146,1,80,0.27)',
                    }, 
                    {
                data: [ 0, 2144820, 2068431, 1959303, 2106626, 1686484, 2226666, 2837781, 2264876 ],
                label: "Costo total",
                backgroundColor: 'rgba(0,198,246,0.31)',
                borderColor: 'rgba(0,198,246,0.31)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(0,198,246,0.31)',
                    }, ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
                
            },
            legend: {
                display: false,
                position: 'top',
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                }


            },
            scales: {
                xAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Año'
                    }
                        } ],
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: true
                    },
                    ticks: { 
                        beginAtZero: true, 
                        callback: function(value, index, values) { 
                         if(parseInt(value) >= 1000){ 
                         return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "."); 
                         } else { 
                         return value; 
                         } 
                        } 
                        },
                    scaleLabel: {
                        display: true,
                        labelString: 'Bs'
                    }
                        } ]
            },
            
            title: {
                display: false,
            }
        }
    } ); 

} )( jQuery );