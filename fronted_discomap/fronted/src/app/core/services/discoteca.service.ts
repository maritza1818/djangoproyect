import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
@Injectable({
    providedIn: 'root'
})
export class DiscotecaService {

    private apiUrl = 'http://127.0.0.1:8000/api/';  // URL de tu API

    constructor(private http: HttpClient) { }

    getDiscotecas(): Observable<any> {
        return this.http.get(`${this.apiUrl}discotecas/`);  // Endpoint para obtener discotecas
    }
    createDiscoteca(discotecaData: any): Observable<any> {
        return this.http.post<any>(this.apiUrl, discotecaData);
      }
   
}

