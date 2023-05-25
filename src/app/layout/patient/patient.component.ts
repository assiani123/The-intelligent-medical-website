import { HttpClient } from '@angular/common/http';
import { Component, ElementRef } from '@angular/core';

import { ShareService } from 'src/app/share.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent {
  k: any
  c: any = 0
  nom: any
  style: any = "none"
  constructor(private http: HttpClient, private elementRef: ElementRef, private share: ShareService, private router: Router) {
    this.http.get("http://127.0.0.1:8000/gnp/" + localStorage.getItem("name"))
      .subscribe((data: any) => {
        this.k = data;
        this.c = data.length;
        const currentDate = new Date();
        const dateTimeString = new Date().toLocaleString();
        console.log(dateTimeString);
      });
    this.nom = localStorage.getItem("name")
  }
  ngAfterViewInit() {
    const element = this.elementRef.nativeElement.querySelector('#l');
    const computedStyle = window.getComputedStyle(element);

    if (computedStyle.display === 'none') {
      element.style.display = 'block';
    } else {
      element.style.display = ''; // ou element.style.display = 'initial'; pour rétablir la valeur par défaut
    }
  }
  g() {
    localStorage.clear();
    this.share.y = false
    this.router.navigate(['/']);
  }
}
