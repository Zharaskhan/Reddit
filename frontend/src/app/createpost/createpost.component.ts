import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-createpost',
  templateUrl: './createpost.component.html',
  styleUrls: ['./createpost.component.css']
})
export class CreatepostComponent implements OnInit {
  public title = '';
  public body = '';
  constructor(private provider: ProviderService,   private router: Router) { }

  ngOnInit() {
    if (!this.provider.isAuthenticated()) {
      this.router.navigate(['/']);
    }
  }

  createPost() {
    if (this.title !== '' && this.body !== '') {
      this.provider.createPost(this.title, this.body);
      this.router.navigate(['/']);
    }
  }
}
