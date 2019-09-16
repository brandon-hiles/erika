import { Component } from '@angular/core';
import { User } from '../../models/user';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})

export class RegisterComponent {

  model = new User(1, 'Brandon', 'Hiles', 'brandon.j.hiles@gmail.com', 'password');
  submitted = false;
  onSubmit() { 
    this.submitted = true; 
    console.log(this.model.email)
  }

  get diagnostic() { return JSON.stringify(this.model); }
}
