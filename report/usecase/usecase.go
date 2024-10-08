package usecase

import "github.com/metalpoch/olt-blueprint/common/model"

type FatUsecase interface {
	Add(fat *model.NewFat) error
	Get(id uint) (*model.Fat, error)
}
