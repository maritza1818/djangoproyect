import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-search-bar',
  standalone: true,
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent {
  @Output() search = new EventEmitter<string>(); 

  searchTerm: string = ''; 

  // entrada de texto
  onInput(event: Event): void {
    const target = event.target as HTMLInputElement;
    this.searchTerm = target.value; 
    this.search.emit(this.searchTerm); 
  }

  //  botón de búsqueda
  onSearchClick(): void {
    this.search.emit(this.searchTerm); 
  }
}
