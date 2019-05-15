import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    
  }

  logout() {
    this.provider.logout();
  }

}
