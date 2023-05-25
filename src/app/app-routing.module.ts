import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MedecinComponent } from './layout/medecin/medecin.component';
import { PatientComponent } from './layout/patient/patient.component';
import { DashComponent } from './views/medecin/dash/dash/dash.component';
import { HomeComponent } from './views/patient/home/home/home.component';

import { RdvmComponent } from './views/medecin/rdvm/rdvm.component';
import { PdvmComponent } from './views/patient/pdvm/pdvm.component';
import { RegpComponent } from './views/patient/regp/regp/regp.component';
import { RegmComponent } from './views/medecin/regm/regm/regm.component';
import { LogComponent } from './views/patient/log/log/log.component';
import { LogmComponent } from './views/medecin/logm/logm.component';
import { CrdvComponent } from './views/patient/crdv/crdv.component';
import { CrmComponent } from './views/medecin/crm/crm.component';
import { ChatpComponent } from './views/patient/chatp/chatp.component';
import { ChatmComponent } from './views/medecin/chatm/chatm.component';
import { EmComponent } from './views/patient/em/em.component';
import { EmmComponent } from './views/medecin/emm/emm.component';
import { PpComponent } from './views/patient/pp/pp.component';
import { GardmGuard } from './gard/gardm.guard';
import { GardpGuard } from './gard/gardp.guard';



const routes: Routes = [
  {
    path: 'medecin', component: MedecinComponent, canActivate: [GardmGuard], canActivateChild: [GardmGuard], children: [
      { path: 'dash', component: DashComponent },
      { path: "rdm", component: CrmComponent },
      { path: 'chatm', component: ChatmComponent },
      { path: 'emm', component: EmmComponent }
    ]



  },
  {
    path: 'patient', component: PatientComponent, canActivate: [GardpGuard], canActivateChild: [GardpGuard], children: [
      { path: 'chatp', component: ChatpComponent },
      { path: "rdv", component: CrdvComponent },


      { path: 'prdv', component: PdvmComponent },
      { path: 'em', component: EmComponent }

    ]



  },
  { path: 'regp', component: RegpComponent },
  { path: 'regm', component: RegmComponent },
  { path: 'log', component: LogComponent },
  { path: 'logm', component: LogmComponent },
  { path: '', component: PpComponent },





];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
