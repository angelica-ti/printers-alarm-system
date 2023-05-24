import {Injectable} from '@angular/core';
import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import Chart from 'chart.js';

// core components
import {
  chartOptions,
  parseOptions,
  chartExample1,
  chartExample2
} from "../../variables/charts";

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})

@Injectable()
export class DashboardComponent implements OnInit{

  public datasets: any;
  public data: any;
  public salesChart;
  public clicked: boolean = true;
  public clicked1: boolean = false;
  public clicked2: boolean = false;
  public failures: any = {};
  public qtySeverities: number[] = [0,0,0]; 
  public qtyBrands: number[] = [0,0,0,0,0,0,0,0]; 
  public qtyCategoriesByType: number[][] = []; 
  public listTypes: string[] = ["laser", "jato", "térmica"];
  public listCategories: string[] = ["driver", "toner", "papel", "cabos", "rolamento", "fusor"]; 
  public listBrands: string[] = ["EPSON", "HP", "BROTHER", "ELGIN", "FUGIFILM", "CANON", "LEXMARK", "ZEBRA", "ARGOX", "XEROX"];
  public totalFailures: number = 0;
  

  ngOnInit() {

    // this.datasets = [
    //   [0, 20, 10, 30, 15, 40],
    //   [0, 20, 5, 25, 10, 30],
    //   [10, 2, 5, 40, 10, 30]
    // ];

    this.getFailureByCategory();
    this.getFailureByBrand();

    this.datasets = this.qtyCategoriesByType;

    this.data = this.datasets[0];

    var chartOrders = document.getElementById('chart-orders');

    parseOptions(Chart, chartOptions());

    chartExample2.data.datasets[0].data = this.qtyBrands;
    var ordersChart = new Chart(chartOrders, {
      type: 'bar',
      options: chartExample2.options,
      data: chartExample2.data
    });

    var chartSales = document.getElementById('chart-sales');

    chartExample1.data.datasets[0].data = this.data;

    this.salesChart = new Chart(chartSales, {
      type: 'bar',
      options: chartExample1.options,
      data: chartExample1.data
    });


  }
  constructor(private http: HttpClient) {
    this.getFailureBySeverity();

  }

  public updateOptions() {
    this.salesChart.data.datasets[0].data = this.data;
    this.salesChart.update();
  }

  public getFailureBySeverity() {

    for(let i = 1; i <= 3; i++){
      var selected = {
        brand: null,
        model: null,
        type: null,
        category: null,
        severity: i
      }
  
      this.http.post('http://localhost:8001/fault-messages/selected', selected).subscribe(
        (response: any = []) =>  {
          this.failures = response;
          this.qtySeverities[i-1] = response.length;
          console.log("Quantidade:");
          console.log(this.qtySeverities);
          console.log("Response:");
          console.log(response);
          this.totalFailures = this.qtySeverities.reduce((acumulador, elemento) => acumulador + elemento, 0);
        },
        error => {
          console.error(error);
        }
      );

    } 
  }

  public getFailureByCategory() {

    for (let i = 0; i < 3; i++) {
      this.qtyCategoriesByType[i] = []; // cria uma nova linha vazia

      for(let j = 0; j < this.listCategories.length; j++){
        var selected = {
          brand: null,
          model: null,
          type: this.listTypes[i],
          category: this.listCategories[j],
          severity: null
        }
    
        this.http.post('http://localhost:8001/fault-messages/selected', selected).subscribe(
          (response: any = []) =>  {
            this.failures = response;
            this.qtyCategoriesByType[i][j] = response.length;
            console.log("Quantidade:");
            console.log(this.qtyCategoriesByType);
            console.log("Response:");
            console.log(response);
          },
          error => {
            console.error(error);
          }
        );
  
      } 
      
    }
 
  }

  public getFailureByBrand() {

    for(let i = 0; i <= this.listBrands.length; i++){
      var selected = {
        brand: this.listBrands[i],
        model: null,
        type: null,
        category: null,
        severity: null,
      }
  
      this.http.post('http://localhost:8001/fault-messages/selected', selected).subscribe(
        (response: any = []) =>  {
          this.failures = response;
          this.qtyBrands[i] = response.length;
          console.log("Quantidade:");
          console.log(this.qtyBrands);
          console.log("Response:");
          console.log(response);
        },
        error => {
          console.error(error);
        }
      );

    } 
  }

}
