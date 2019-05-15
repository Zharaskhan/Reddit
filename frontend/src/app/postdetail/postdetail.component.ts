import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {IPOST} from '../shared/models';
import {ActivatedRoute} from '@angular/router';
import {MainService} from '../shared/services/main.service';

@Component({
  selector: 'app-postdetail',
  templateUrl: './postdetail.component.html',
  styleUrls: ['./postdetail.component.css']
})
export class PostdetailComponent implements OnInit {
  public post: IPOST;
  constructor(private provider: ProviderService,  private route: ActivatedRoute, private main: MainService) { }

  ngOnInit() {
    const id = +this.route.snapshot.paramMap.get('id');

    this.provider.getPost(id).then(res => {
      this.post = res;
      setTimeout(() => {
      }, 5000);
    });
  }

}
