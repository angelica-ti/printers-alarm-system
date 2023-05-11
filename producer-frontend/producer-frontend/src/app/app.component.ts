import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { interval } from 'rxjs';

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
  showSuccess: boolean = false;

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
          this.showSuccess = true;
          interval(3000).subscribe(() => {
            this.showSuccess = false;
          });
          console.log(response);
        },
        error => {
          console.error(error);
        }
      );
  }

  

}


