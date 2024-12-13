export class Discoteca {
    id: number;
    nombre: string;
    direccion: string;
    horario_apertura: string;
    horario_cierre: string;
    aforo_maximo: number;
    stock_bebidas: number;
    calificacion: number;
    descripcion: string;
    created_at: string;
    imagen: string;
    user: any;  // Esto lo puedes ajustar según lo que devuelva el `UserSerializer` en tu API.
  
    constructor(
      id: number,
      nombre: string,
      direccion: string,
      horario_apertura: string,
      horario_cierre: string,
      aforo_maximo: number,
      stock_bebidas: number,
      calificacion: number,
      descripcion: string,
      created_at: string,
      imagen: string,
      user: any
    ) {
      this.id = id;
      this.nombre = nombre;
      this.direccion = direccion;
      this.horario_apertura = horario_apertura;
      this.horario_cierre = horario_cierre;
      this.aforo_maximo = aforo_maximo;
      this.stock_bebidas = stock_bebidas;
      this.calificacion = calificacion;
      this.descripcion = descripcion;
      this.created_at = created_at;
      this.imagen = imagen || 'assets/default-image.jpg';
      this.user = user;
    }
  }
  