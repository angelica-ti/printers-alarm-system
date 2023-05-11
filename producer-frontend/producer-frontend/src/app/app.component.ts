import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  brand: string = '';
  model: string = '';
  type: string = '';
  category: string = '';
  severity: number = 1;
  description: string = '';

  constructor(private http: HttpClient) { }

  sendData() {
    const dados = {
      brand: this.brand,
      model: this.model,
      type: this.type,
      category: this.category,
      severity: this.severity,
      description: this.description
    };

    this.http.post('http://localhost:8000/send-message', dados)
      .subscribe(
        response => {
          console.log(response);
          // Lógica adicional após o envio dos dados
        },
        error => {
          console.error(error);
          // Lógica adicional em caso de erro
        }
      );
  }

  

}


