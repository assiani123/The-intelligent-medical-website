import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-chatm',
  templateUrl: './chatm.component.html',
  styleUrls: ['./chatm.component.css']
})
export class ChatmComponent {
  c: any;
  k: any = [];
  l: any

  constructor(private http: HttpClient) {
    this.c = localStorage.getItem('name');
    this.getData();
  }

  getData() {
    this.http.get('http://127.0.0.1:8000/msgm/' + this.c).subscribe((data) => {
      console.log(data)
      this.k = data
      this.l = this.k.length
      console.log(this.l)

    });
  }

  po(form: NgForm) {
    const d = form.value;
    console.log(d);
    d["nome"] = this.c;
    d["nomc"] = "cm";
    console.log(d);
    this.http.post('http://127.0.0.1:8000/mm/', d).subscribe(data => {
      console.log(data);
      this.getData(); // Mettre à jour les données
    });
  }
}
