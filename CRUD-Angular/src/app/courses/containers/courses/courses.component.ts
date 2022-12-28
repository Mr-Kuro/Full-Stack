import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute, Router } from '@angular/router';
import { catchError, Observable, of } from 'rxjs';
import { ErrorDialogComponent } from 'src/app/shared/components/error-dialog/error-dialog.component';
import { Course } from '../../interfaces/course';
import { CoursesService } from '../../services/courses.service';

@Component({
  selector: 'app-courses',
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.scss']
})
export class CoursesComponent implements OnInit {

  // observables de curses[] e apenas Curse[]
  // public coursees: Course[] = [];    // teste* apenas Curse[]
  public courses$: Observable<Course[]> = of([]);    // observable de Curse[]

  /*
    // array de colunas para mostrar no mat...
    public displayedColumns = [/*'_id',/ 'name', 'category', 'duration', 'actions'];
  */

  // coursesService: CoursesService;  // outra forma de inicializar fora do construtor da classe

  constructor(
    private coursesService: CoursesService,
    public dialog: MatDialog,
    private router: Router,
    private route: ActivatedRoute,
    private _snackBar: MatSnackBar,
  ) {
    this.reFresh()
  }

  reFresh() {
    this.courses$ = this.coursesService.list().pipe(
      catchError(error => {
        // console.log(error)
        this.onError("Erro ao carregar Cursos Disponíveis!\n verifique a conexão com a internet")
        return of([]);
      })
    );
  }

  onError(errorMsg: string) {
    this.dialog.open(ErrorDialogComponent, {
      data:
        errorMsg
    })
  }

  onAdd() {
    console.log('On Add')
    this.router.navigate(['new'], { relativeTo: this.route })
  }

  onEdit(course: Course) {
    this.router.navigate(['edit', course._id], { relativeTo: this.route })
  }

  onDelete(course: Course) {
    if (course._id) {
      this.coursesService.delete(course._id).subscribe(
        () => {
          this._snackBar.open("Sucesso ao Deletar curso", "close", {
            duration: 5000,
            verticalPosition: 'top',
            horizontalPosition: 'center'
          });
        },
        () => this.onError("Erro ao deletar Curso!"))

      this.reFresh();
    };

  }

  ngOnInit(): void { }

}
