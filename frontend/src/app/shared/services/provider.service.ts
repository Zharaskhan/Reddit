import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import {HttpClient} from '@angular/common/http';
import {IAuthResponse, ICOMMENT, IPOST} from '../models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) { super(http); }

  isAuthenticated(): boolean {
    return !!localStorage.getItem('token');
  }

  auth(login: any, password: any): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: login,
      password
    });
  }

  logout(): void {
    this.post('http://localhost:8000/api/logout/', {}).then(() => {
      localStorage.clear();
    });
  }

  getPosts(): Promise<IPOST[]> {
    return this.get('http://localhost:8000/api/posts/', {});
  }

  getPost(id: number): Promise<IPOST> {
    return this.get(`http://localhost:8000/api/posts/${id}/`, {});
  }


  createPost(title: string, body: string): Promise<IPOST> {
    return this.post('http://localhost:8000/api/posts/', {
      name,
      body,
    });
  }

  createComment(id: number, text: string): Promise<ICOMMENT> {
    return this.post(`http://localhost:8000/api/posts/${id}/comments/`, {
      text
    });
  }
/*
  getContact(id: number): Promise<IContact> {
    return this.get(`http://localhost:8000/api/contacts/${id}/`, {});
  }

  updateContact(contact: IContact): Promise<IContact> {
    return this.put(`http://localhost:8000/api/contacts/${contact.id}/`, {
      name: contact.name,
      phone: contact.phone
    });
  }

  deleteContact(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/contacts/${id}/`, {});
  }
 */
}
