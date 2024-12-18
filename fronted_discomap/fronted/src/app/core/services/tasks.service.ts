import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Project } from '../../models/projects.model';

@Injectable({
  providedIn: 'root',
})
export class TasksService {
  private apiUrl = 'http://localhost:8000/api/projects/'; 

  constructor(private http: HttpClient) {}

  getTasks(): Observable<Project[]> {
    return this.http.get<Project[]>(this.apiUrl);
  }
}
