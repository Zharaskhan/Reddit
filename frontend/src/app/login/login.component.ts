import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public username = '';
  public password = '';

  constructor(private provider: ProviderService,   private router: Router) { }

  ngOnInit() {
  }

  login() {
    if (this.username !== '' && this.password !== '') {
      this.provider.auth(this.username, this.password).then(res => {
        localStorage.setItem('token', res.token);
      });
      this.router.navigate(['/']);
    }
  }

}
