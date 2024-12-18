import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private loginUrl = 'http://localhost:8000/api/usuarios/login/';
  private registerUrl = 'http://localhost:8000/api/usuarios/register/';
  private discotecasUrl = 'http://localhost:8000/api/discotecas/';
  
  private isAuthenticatedSubject = new BehaviorSubject<boolean>(this.hasToken());

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<any> {
    return this.http.post<any>(this.loginUrl, { username, password }).pipe(
      tap((response: any) => {  
        localStorage.setItem('token', response.token);
        localStorage.setItem('username', username);
        this.isAuthenticatedSubject.next(true);
      })
    );
  }

  register(username: string, password1: string, password2: string): Observable<any> {
    return this.http.post<any>(this.registerUrl, { username, password1, password2 }).pipe(
      tap((response: any) => {
        localStorage.setItem('token', response.token);
        localStorage.setItem('username', username);
        this.isAuthenticatedSubject.next(true);
      })
    );
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    this.isAuthenticatedSubject.next(false);
  }

  isAuthenticated(): Observable<boolean> {
    return this.isAuthenticatedSubject.asObservable();
  }

  getUsername(): string | null {
    return localStorage.getItem('username');
  }

  private hasToken(): boolean {
    return localStorage.getItem('token') !== null;
  }
}
