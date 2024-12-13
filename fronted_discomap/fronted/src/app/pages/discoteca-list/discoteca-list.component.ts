import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { CardDiscotecaComponent } from '../../components/card-discoteca/card-discoteca.component'; // Asegúrate de tener este componente
import { DiscotecaService } from '../../core/services/discoteca.service';
import { Discoteca } from '../../models/discoteca.model';

@Component({
  selector: 'app-discoteca-list',
  templateUrl: './discoteca-list.component.html',
  styleUrls: ['./discoteca-list.component.css'],
  standalone: true,
  imports: [CardDiscotecaComponent, CommonModule]
})
export class DiscotecaListComponent implements OnInit {
  discotecas: Discoteca[] = [];  // Array para almacenar discotecas

  constructor(private discotecaService: DiscotecaService) {}

  ngOnInit(): void {
    this.loadDiscotecas();
  }

  loadDiscotecas(): void {
    this.discotecaService.getDiscotecas().subscribe(
      (data: Discoteca[]) => {
        console.log('Discotecas obtenidas:', data);
        this.discotecas = data;  // Asigna las discotecas al array
      },
      (error) => {
        console.error('Error al obtener discotecas:', error);
      }
    );
  }
}
