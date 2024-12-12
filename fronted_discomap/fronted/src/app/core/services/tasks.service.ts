import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TasksService {

  private apiUrl = 'http://127.0.0.1:8000/api/'; // Aquí debe ir la URL de tu API

  constructor(private http: HttpClient) { }

  getDiscotecas(): Observable<any> {
    return this.http.get(`${this.apiUrl}discotecas/`);  // Endpoint para obtener discotecas
  }

  getTasks(): Observable<any> {
    return this.http.get(`${this.apiUrl}tasks/`);  // Endpoint para obtener tareas
  }
}