import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { NonNullableFormBuilder, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute } from '@angular/router';
import { ErrorDialogComponent } from 'src/app/shared/components/error-dialog/error-dialog.component';
import { Course } from '../../interfaces/course';
import { CoursesService } from '../../services/courses.service';

@Component({
  selector: 'app-course-form',
  templateUrl: './course-form.component.html',
  styleUrls: ['./course-form.component.scss']
})
export class CourseFormComponent implements OnInit {

  public courseForm = this.formBiulder.group<Course>({
    _id: ''
    // ['']
    ,
    name: ''
    // ['',
    //   Validators.required,
    //   Validators.maxLength(200),
    //   Validators.minLength(3)
    // ]
    ,
    category: ''
    // ['',
    //   Validators.required,
    //   Validators.maxLength(10),
    //   Validators.minLength(3)
    // ]
    ,
    duration: ''
    // ['',
    //   Validators.required,
    //   Validators.maxLength(100),
    // ]
    ,
  });

  constructor(
    private formBiulder: NonNullableFormBuilder,
    private service: CoursesService,
    private dialog: MatDialog,
    private _snackBar: MatSnackBar,
    private location: Location,
    private route: ActivatedRoute,
  ) {
  }

  onSubmit() {
    this.service.save(this.courseForm.value).subscribe(
      result => { console.log(result); this.onSave() },
      error => { console.error(error); this.onError() }
    );

  }

  onCancel(): void {
    this.location.back();
    console.log("cancel")
  };

  onSave() {
    this._snackBar.open("Sucesso ao salvar curso", "close", {
      duration: 5000,
      panelClass: "snackbar",
      announcementMessage: "gay"

    });
    this.onCancel();
  }
  // console.log("SuccesMsg")

  onError() {
    this.dialog.open(ErrorDialogComponent, {
      data: "Erro ao salvar Curso!\n verifique a conexão com a internet",
    })
    // console.log("MsgError")
  }

  getErrorMessage(fieldName: string) {
    const field = this.courseForm.get(fieldName)

    if (field?.hasError('required')) {
      return 'Campo obrigatório';
    };

    if (field?.hasError('minlength')) {
      const requiredLength: number = field.errors ? field.errors['minlength']['requiredlength'] : 3;
      return `tamanho mínimo do campo é ${requiredLength} caracteres`;
    };

    if (field?.hasError('maxlength')) {
      const requiredLength: number = field.errors ? field.errors['maxlength']['requiredlength'] : 200;
      return `tamanho máximo de ${requiredLength} caracteres foi excedido`;
    };

    return 'Campo iválido!';
  }


  ngOnInit(): void {
    const course = this.route.snapshot.data['course']
    this.courseForm.setValue(
      {
        _id: course._id,
        name: course.name,
        category: course.category,
        duration: course.duration,
      }

    )
    console.log(this.courseForm.value.duration)
  };

}
