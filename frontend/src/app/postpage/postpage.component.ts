import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {IPOST} from '../shared/models';
import {MainService} from '../shared/services/main.service';

@Component({
  selector: 'app-parent',
  templateUrl: './postpage.component.html',
  styleUrls: ['./postpage.component.css']
})
export class PostpageComponent implements OnInit {

  public posts: IPOST[] = [];

  constructor(private provider: ProviderService, private main: MainService) {
  }

  ngOnInit() {
    this.provider.getPosts().then(re