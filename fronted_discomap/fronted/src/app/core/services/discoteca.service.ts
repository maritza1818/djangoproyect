import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Discoteca } from '../../models/discoteca.model';

@Injectable({
    providedIn: 'root'
})
export class DiscotecaService {
    private apiUrl = 'http://127.0.0.1:8000/api/';  // URL de tu API

    constructor(private http: HttpClient) { }

    getDiscotecas(): Observable<Discoteca[]> {
        return this.http.get<Discoteca[]>(`${this.apiUrl}discotecas/`)
          .pipe(
            catchError(this.handleError)
          );
    }

    createDiscoteca(discotecaData: Discoteca): Observable<Discoteca> {
        const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
        return this.http.post<Discoteca>(`${this.apiUrl}discotecas/`, discotecaData, { headers })
          .pipe(
            catchError(this.handleError)
          );
    }

    private handleError(error: any): Observable<never> {
        console.error('An error occurred', error);
        return throwError(() => new Error('Something bad happened; please try again later.'));
    }
}
