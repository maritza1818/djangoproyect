import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { CardDiscotecaComponent } from '../../components/card-discoteca/card-discoteca.component'; 
import { SearchBarComponent } from '../../components/search-bar/search-bar.component';
import { DiscotecaService } from '../../core/services/discoteca.service';
import { Discoteca } from '../../models/discoteca.model';

@Component({
  selector: 'app-discoteca-list',
  templateUrl: './discoteca-list.component.html',
  styleUrls: ['./discoteca-list.component.css'],
  standalone: true,
  imports: [CardDiscotecaComponent, CommonModule,  SearchBarComponent]
})
export class DiscotecaListComponent implements OnInit {
  discotecas: Discoteca[] = [];
  filteredDiscotecas: Discoteca[] = []; 
  searchTerm: string = ''; 
  constructor(private discotecaService: DiscotecaService) {}

  ngOnInit(): void {
    this.loadDiscotecas();
  }

  loadDiscotecas(): void {
    this.discotecaService.getDiscotecas().subscribe(
      (data: Discoteca[]) => {
        console.log('Discotecas obtenidas:', data);
        this.discotecas = data;  
        this.filteredDiscotecas = data;
      },
      (error) => {
        console.error('Error al obtener discotecas:', error);
      }
    );
  }
  //funcion que filtra la disocteca
  onSearch(term: string): void {
    this.searchTerm = term;
    this.filteredDiscotecas = this.discotecas.filter((discoteca) =>
      discoteca.nombre.toLowerCase().includes(term.toLowerCase())
    );
  }
}
