import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PatientComponent } from './patient/patient.component';
import { MedecinComponent } from './medecin/medecin.component';
import { RouterModule } from '@angular/router';






@NgModule({
  declarations: [
    PatientComponent,
    MedecinComponent,



  ],
  imports: [
    CommonModule,
    RouterModule

  ]
})
export class LayoutModule { }
