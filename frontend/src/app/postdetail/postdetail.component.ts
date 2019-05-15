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
  public post_list: IPOST[] = [];
  public text = '';

  public title: any='';
  public body: any='';
  public mode: String='';

  constructor(private provider: ProviderService,  private route: ActivatedRoute, private main: MainService) { }

  ngOnInit() {
    const id = +this.route.snapshot.paramMap.get('id');

    this.provider.getPost(id).then(res => {
      this.post = res;
      setTimeout(() => {
      }, 5000);
    });
  }

  createComment() {
    if (this.text !== '') {
      const id = +this.route.snapshot.paramMap.get('id');
      this.provider.createComment(id, this.text).then(res => {
        this.text = '';
        this.post.post_comments += 1;
        this.post.comments.push(res);
      });
    }
  }


  deletePost(id: number){
    this.provider.deletePost(id).then(res => {
      for( let i = 0; i < this.post_list.length; i++){
        if ( this.post_list[i].id === id) {
          this.post_list.splice(i, 1);
        }
      }
    })
  }

  updatePost(){
    if(this.title != ''){
      this.post.title = this.title;
      this.post.body = this.body;
      this.provider.updatePost(this.post).then(res => {
        for (let i = 0; i < this.post_list.length; i++){
          if (this.post_list[i].id == this.post.id){
            this.post_list[i].title = this.title;
            this.post_list[i].body = this.body;
          }
        }
        this.title = '';
        this.body = '';
      })
    }
    this.changeMode('update_post');
  }


  changeMode(mode: String){
    this.mode = mode;
  }

}
