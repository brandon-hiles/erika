import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from  '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavComponent } from './nav/nav.component';

// Main Components
import { HomeComponent } from './main/home/home.component';
import { LoginComponent } from './main/login/login.component';
import { RegisterComponent } from './main/register/register.component';
import { GetStartedComponent } from './main/get-started/get-started.component';

// Admin Components
import { DashboardComponent } from './admin/dashboard/dashboard.component';
import { ArticlesComponent } from './admin/articles/articles.component';
import { LogoutComponent } from './admin/logout/logout.component';
import { SettingsComponent } from './admin/settings/settings.component';

// Footer Components
import { AboutComponent } from './footer/about/about.component';
import { LegalComponent } from './footer/legal/legal.component';
import { PrivacyComponent } from './footer/privacy/privacy.component';

@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    HomeComponent,
    LoginComponent,
    RegisterComponent,
    GetStartedComponent,
    DashboardComponent,
    ArticlesComponent,
    LogoutComponent,
    SettingsComponent,
    AboutComponent,
    LegalComponent,
    PrivacyComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
