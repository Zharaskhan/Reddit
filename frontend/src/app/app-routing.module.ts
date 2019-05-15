import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponent} from './login/login.component';
import {AppComponent} from './app.component';
import {PostpageComponent} from './postpage/postpage.component';
import {PostdetailComponent} from './postdetail/postdetail.component';
import {CreatepostComponent} from './createpost/createpost.component';

const routes: Routes = [
  {path: '', component: PostpageComponent},
  {path: 'posts', component: PostpageComponent},
  {path: 'posts/:id', component: PostdetailComponent},
  {path: 'login', component: LoginComponent},
  {path: 'create_post', component: CreatepostComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
