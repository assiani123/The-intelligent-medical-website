import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { LayoutModule } from './layout/layout.module';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { PdvmComponent } from './views/patient/pdvm/pdvm.component';
import { HttpClientModule } from '@angular/common/http';
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




@NgModule({
  declarations: [
    AppComponent, PdvmComponent, RegpComponent, RegmComponent, LogComponent, LogmComponent, CrdvComponent, CrmComponent, ChatpComponent, ChatmComponent, EmComponent, EmmComponent, PpComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatSlideToggleModule,
    MatToolbarModule,
    MatIconModule,
    LayoutModule,
    RouterModule,
    CommonModule,
    FormsModule,
    HttpClientModule

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
