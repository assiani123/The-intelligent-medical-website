import { HttpClient } from '@angular/common/http';
import { Component, ElementRef } from '@angular/core';
import { Router } from '@angular/router'; // Corrected import statement
import { ShareService } from 'src/app/share.service';

@Component({
  selector: 'app-medecin',
  templateUrl: './medecin.component.html',
  styleUrls: ['./medecin.component.css']
})
export class MedecinComponent {
  k: any;
  c: any = 0;
  nom: any;

  constructor(private http: HttpClient, private elementRef: ElementRef, private router: Router, private share: ShareService) {
    this.http.get("http://127.0.0.1:8000/gnm/" + localStorage.getItem("name")).subscribe((data: any) => {
      this.k = data;
      this.c = data.length;
    });
    this.nom = localStorage.getItem("name");
  }

  ngAfterViewInit() {
    const element = this.elementRef.nativeElement.querySelector('#l');
    const computedStyle = window.getComputedStyle(element);

    if (computedStyle.display == 'none') {
      element.style.display = 'block';
    } else {
      element.style.display = 'none';
    }
  }

  g() {
    localStorage.clear();
    this.share.x = false
    this.router.navigate(['/']);
  }
}