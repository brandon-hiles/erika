import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

// Main Components
import { HomeComponent } from './main/home/home.component';
import { GetStartedComponent } from './main/get-started/get-started.component';
import { RegisterComponent } from './main/register/register.component';
import { LoginComponent } from './main/login/login.component';

// Admin Components
import { DashboardComponent } from './admin/dashboard/dashboard.component';
import { ArticlesComponent } from './admin/articles/articles.component';
import { LogoutComponent } from './admin/logout/logout.component';
import { SettingsComponent } from './admin/settings/settings.component';

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'get-started', component: GetStartedComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'login', component: LoginComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
